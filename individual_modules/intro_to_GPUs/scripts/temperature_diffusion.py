"""
3D Temperature Diffusion Simulation

This module implements a simple 3D temperature diffusion model using three backends:
- NumPy (CPU)
- CuPy (GPU)
- Pure Python nested lists

Functions:
- load_data: Load ocean temperature data from a NetCDF file.
- save_to_netcdf: Save computed temperature fields back to NetCDF.
- temperature_diffusion_numpy: Run diffusion with NumPy arrays.
- temperature_diffusion_cupy: Run diffusion on GPU via CuPy.
- temperature_diffusion_purepython: Naive pure-Python implementation.
- run_diffusion_*: Entry points for CLI execution.
"""


# -------------------------------------------------------------------
# Library imports
# -------------------------------------------------------------------

import xarray as xr
from pathlib import Path
import argparse
import time
import xarray as xr
import numpy as np
import cupy as cp
from tqdm import tqdm 
import math
import copy

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------

# Define the project root directory (two levels up from this file)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Directory containing NetCDF input data
DATA_DIR = ROOT_DIR / "model_data"

# NetCDF input filename (globe, 6-hourly, thetao variable)
DATA_FILE = "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_thetao_13.83W-6.17E_46.83N-65.25N_0.49-5727.92m_2024-01-01-2024-01-01.nc"

# Filenames for each output implementation
OUTPUT_FILE_NUMPY = "predicted_temperatures_numpy.nc"
OUTPUT_FILE_CUPY = "predicted_temperatures_cupy.nc"
OUTPUT_FILE_PUREPYTHON = "predicted_temperatures_purepython.nc"

# -------------------------------------------------------------------
# Data I/O functions
# -------------------------------------------------------------------


def load_data():
    """
    Load the ocean temperature dataset from a NetCDF file.

    The file path is constructed from DATA_DIR and DATA_FILE constants.

    Returns:
        xr.Dataset: An xarray Dataset containing the loaded data.
    """
    file_path = DATA_DIR / DATA_FILE
    return xr.open_dataset(file_path)


def save_to_netcdf(data, new_temperature, output_file_path, num_timesteps):
    """
    Save a modified temperature array to a NetCDF file.

    Adjusts the temperature array to match the specified number of timesteps
    and constructs a new xarray Dataset with the original spatial coordinates.

    Args:
        data (xr.Dataset): Original dataset containing depth, latitude, longitude.
        new_temperature (np.ndarray): Array of shape (time, depth, lat, lon)
            containing the updated temperatures.
        output_file_path (Path or str): Path to write the new NetCDF file.
        num_timesteps (int): Number of timesteps to include in the output.
    """
    # Adjust new_temperature to have only num_timesteps or fewer
    new_temperature = new_temperature[:num_timesteps]  # Only include the desired number of timesteps

    # Generate a new time coordinate as a sequence of numbers (1, 2, ..., num_timesteps)
    time_coord = range(1, num_timesteps + 1)

    # Create a new dataset with original depth, latitude, and longitude coordinates
    output_data = xr.Dataset(
        {'thetao': (('time', 'depth', 'latitude', 'longitude'), new_temperature)},
        coords={
            'time': time_coord,  # Sequential time coordinate
            'depth': data['depth'].values,  # Use original depth coordinates
            'latitude': data['latitude'].values,  # Use original latitude coordinates
            'longitude': data['longitude'].values  # Use original longitude coordinates
        },
    )
    output_data.to_netcdf(output_file_path, engine='netcdf4')

# -------------------------------------------------------------------
# Diffusion model implementations
# -------------------------------------------------------------------

# Temperature diffusion function using NumPy with masking for boundaries
def temperature_diffusion_numpy(data, num_timesteps, diffusion_coeff=0.1):
    """
    Simulate temperature diffusion over time using NumPy arrays.

    A simple 3D diffusion stencil is applied across the ocean grid,
    with NaN regions (land) masked out.

    Args:
        data (xr.Dataset): Input dataset containing the 'thetao' variable.
        num_timesteps (int): Number of timesteps to simulate.
        diffusion_coeff (float, optional): Diffusion coefficient. Defaults to 0.1.

    Side effects:
        - Saves the resulting temperature field to a NetCDF file (OUTPUT_FILE_NUMPY).
        - Prints timing statistics to stdout.
    """
    temperature = np.asarray(data['thetao'].values)  # Convert to a NumPy array
    temperature = temperature[0:1, :, :, :]
    temperature = np.tile(temperature, (num_timesteps, 1, 1, 1))
    
    mask = ~np.isnan(temperature)  # Mask: True for ocean points, False for NaN regions (land)
    new_temperature = np.copy(temperature)
    timestep_durations = []

    # Extract the first timestamp and create a new time coordinate for the predicted timesteps
    original_time = data['time'].values
    time_coord = np.array([original_time[0] + np.timedelta64(i, 'D') for i in range(num_timesteps)])

    # Run the diffusion model
    for t in tqdm(range(num_timesteps), desc="NumPy Diffusion Progress"):
        start_time = time.time()

        # Apply diffusion calculation with mask-based boundary handling
        temp_copy = temperature[1:-1, 1:-1, 1:-1]  # Core section without boundaries
        neighbor_sum = np.zeros_like(temp_copy)
        neighbor_count = np.zeros_like(temp_copy)

        # Sum available neighbors and count them only for valid ocean points
        if mask[:-2, 1:-1, 1:-1].any():  # Front
            neighbor_sum += np.where(mask[:-2, 1:-1, 1:-1], temperature[:-2, 1:-1, 1:-1], 0)
            neighbor_count += mask[:-2, 1:-1, 1:-1]

        if mask[2:, 1:-1, 1:-1].any():  # Back
            neighbor_sum += np.where(mask[2:, 1:-1, 1:-1], temperature[2:, 1:-1, 1:-1], 0)
            neighbor_count += mask[2:, 1:-1, 1:-1]

        if mask[1:-1, :-2, 1:-1].any():  # Left
            neighbor_sum += np.where(mask[1:-1, :-2, 1:-1], temperature[1:-1, :-2, 1:-1], 0)
            neighbor_count += mask[1:-1, :-2, 1:-1]

        if mask[1:-1, 2:, 1:-1].any():  # Right
            neighbor_sum += np.where(mask[1:-1, 2:, 1:-1], temperature[1:-1, 2:, 1:-1], 0)
            neighbor_count += mask[1:-1, 2:, 1:-1]

        if mask[1:-1, 1:-1, :-2].any():  # Bottom
            neighbor_sum += np.where(mask[1:-1, 1:-1, :-2], temperature[1:-1, 1:-1, :-2], 0)
            neighbor_count += mask[1:-1, 1:-1, :-2]

        if mask[1:-1, 1:-1, 2:].any():  # Top
            neighbor_sum += np.where(mask[1:-1, 1:-1, 2:], temperature[1:-1, 1:-1, 2:], 0)
            neighbor_count += mask[1:-1, 1:-1, 2:]

        # Apply diffusion to valid points only, avoiding NaN regions
        new_temperature[1:-1, 1:-1, 1:-1] = np.where(
            mask[1:-1, 1:-1, 1:-1],
            temp_copy + diffusion_coeff * (neighbor_sum - 6 * temp_copy) / np.maximum(neighbor_count, 1),
            temperature[1:-1, 1:-1, 1:-1]
        )

        timestep_durations.append(time.time() - start_time)
        temperature = new_temperature
        
    # Convert to final temperature and save
    final_temperature = new_temperature
    
    # Save to NetCDF (assuming you have a `save_to_netcdf` function defined)
    save_to_netcdf(data, final_temperature, DATA_DIR / OUTPUT_FILE_NUMPY, num_timesteps)

    avg_time_per_timestep = sum(timestep_durations) / num_timesteps
    print(f"NumPy model completed in {sum(timestep_durations):.4f} seconds. "
          f"Average time per timestep: {avg_time_per_timestep:.4f} seconds.")


    
def run_diffusion_numpy():
    """
    Entry point for running the NumPy diffusion model via command line.

    Parses --num_timesteps and invokes temperature_diffusion_numpy().
    """
    parser = argparse.ArgumentParser(description="Run 3D Diffusion Model with Numpy")
    parser.add_argument("--num_timesteps", type=int, default=300, help="Number of Timesteps to run for")

    args = parser.parse_args()

    # Pass parsed arguments to visualisation_slice
    temperature_diffusion_numpy(data=load_data(), num_timesteps=args.num_timesteps)

# # Temperature diffusion function using CuPy with masking for boundaries
def temperature_diffusion_cupy(data, num_timesteps, diffusion_coeff=0.5):
    """
    Simulate temperature diffusion over time using CuPy (GPU acceleration).

    Similar stencil as the NumPy version, but runs on the GPU.
    Data is converted back to NumPy before saving.

    Args:
        data (xr.Dataset): Input dataset containing 'thetao'.
        num_timesteps (int): Number of timesteps to simulate.
        diffusion_coeff (float, optional): Diffusion coefficient. Defaults to 0.5.

    Side effects:
        - Saves the resulting field to a NetCDF file (OUTPUT_FILE_CUPY).
        - Prints timing statistics.
    """
    temperature = cp.asarray(data['thetao'].values)  # Convert to a CuPy array
    temperature = temperature[0:1, :, :, :]
    temperature = np.tile(temperature, (num_timesteps, 1, 1, 1))

    mask = ~cp.isnan(temperature)  # Mask: True for ocean points, False for NaN regions (land)
    new_temperature = cp.copy(temperature)
    timestep_durations = []

    # Extract the first timestamp and create a new time coordinate for the predicted timesteps
    original_time = data['time'].values
    time_coord = np.array([original_time[0] + np.timedelta64(i, 'D') for i in range(num_timesteps)])

    # Run the diffusion model
    for t in tqdm(range(num_timesteps), desc="CuPy Diffusion Progress"):
        start_time = time.time()

        # Apply diffusion calculation with mask-based boundary handling
        temp_copy = temperature[1:-1, 1:-1, 1:-1]  # Core section without boundaries
        neighbor_sum = cp.zeros_like(temp_copy)
        neighbor_count = cp.zeros_like(temp_copy)

        # Sum available neighbors and count them only for valid ocean points
        if mask[:-2, 1:-1, 1:-1].any():  # Front
            neighbor_sum += cp.where(mask[:-2, 1:-1, 1:-1], temperature[:-2, 1:-1, 1:-1], 0)
            neighbor_count += mask[:-2, 1:-1, 1:-1]

        if mask[2:, 1:-1, 1:-1].any():  # Back
            neighbor_sum += cp.where(mask[2:, 1:-1, 1:-1], temperature[2:, 1:-1, 1:-1], 0)
            neighbor_count += mask[2:, 1:-1, 1:-1]

        if mask[1:-1, :-2, 1:-1].any():  # Left
            neighbor_sum += cp.where(mask[1:-1, :-2, 1:-1], temperature[1:-1, :-2, 1:-1], 0)
            neighbor_count += mask[1:-1, :-2, 1:-1]

        if mask[1:-1, 2:, 1:-1].any():  # Right
            neighbor_sum += cp.where(mask[1:-1, 2:, 1:-1], temperature[1:-1, 2:, 1:-1], 0)
            neighbor_count += mask[1:-1, 2:, 1:-1]

        if mask[1:-1, 1:-1, :-2].any():  # Bottom
            neighbor_sum += cp.where(mask[1:-1, 1:-1, :-2], temperature[1:-1, 1:-1, :-2], 0)
            neighbor_count += mask[1:-1, 1:-1, :-2]

        if mask[1:-1, 1:-1, 2:].any():  # Top
            neighbor_sum += cp.where(mask[1:-1, 1:-1, 2:], temperature[1:-1, 1:-1, 2:], 0)
            neighbor_count += mask[1:-1, 1:-1, 2:]

        # Apply diffusion to valid points only, avoiding NaN regions
        new_temperature[1:-1, 1:-1, 1:-1] = cp.where(
            mask[1:-1, 1:-1, 1:-1],
            temp_copy + diffusion_coeff * (neighbor_sum - 6 * temp_copy) / cp.maximum(neighbor_count, 1),
            temperature[1:-1, 1:-1, 1:-1]
        )

        cp.cuda.Stream.null.synchronize()  # Wait for the GPU computation to complete
        timestep_durations.append(time.time() - start_time)
        temperature = new_temperature

        
    # Convert back to NumPy and save
    final_temperature = cp.asnumpy(new_temperature)


    save_to_netcdf(data, final_temperature, DATA_DIR / OUTPUT_FILE_CUPY, num_timesteps)

    avg_time_per_timestep = sum(timestep_durations) / num_timesteps
    print(f"CuPy model completed in {sum(timestep_durations):.4f} seconds. "
          f"Average time per timestep: {avg_time_per_timestep:.4f} seconds.")

    
def run_diffusion_cupy():
    """
    Entry point for running the CuPy diffusion model via command line.

    Parses --num_timesteps and calls temperature_diffusion_cupy().
    """
    parser = argparse.ArgumentParser(description="Run 3D Diffusion Model with CuPy")
    parser.add_argument("--num_timesteps", type=int, default=300, help="Number of Timesteps to run for")

    args = parser.parse_args()

    # Pass parsed arguments to visualisation_slice
    temperature_diffusion_cupy(data=load_data(), num_timesteps=args.num_timesteps)


def temperature_diffusion_purepython(data, num_timesteps, diffusion_coeff=0.1):
    """
    Simulate temperature diffusion using pure Python nested loops and lists.

    This implementation is the simplest (and slowest), building Python lists
    and manually iterating over every grid cell.

    Args:
        data (xr.Dataset): Dataset containing 'thetao'.
        num_timesteps (int): Number of timesteps to simulate.
        diffusion_coeff (float, optional): Diffusion coefficient. Defaults to 0.1.

    Side effects:
        - Saves the resulting field to a NetCDF file (OUTPUT_FILE_PUREPYTHON).
        - Prints timing statistics.
    """
    # Pull raw array and get dims
    raw = data['thetao'].values              # shape (time, depth, lat, lon)
    depth, lat, lon = raw.shape[1], raw.shape[2], raw.shape[3]

    # Initial snapshot at t=0, as Python lists
    initial = raw[0]                         # shape (depth, lat, lon)
    temperature = []
    for _ in range(num_timesteps):
        # deep copy initial for each timestep
        plane = []
        for d in range(depth):
            plane.append([ [ float(initial[d][i][j]) for j in range(lon) ]
                           for i in range(lat) ])
        temperature.append(plane)

    # Summary stats (very slow!)
    flat = []
    for t in range(num_timesteps):
        for d in range(depth):
            for i in range(lat):
                for j in range(lon):
                    v = temperature[t][d][i][j]
                    if not math.isnan(v):
                        flat.append(v)
    flat_sorted = sorted(flat)

    # Precompute mask of valid ocean points
    mask = [[[ [ not math.isnan(temperature[t][d][i][j])
                 for j in range(lon) ]
               for i in range(lat) ]
             for d in range(depth) ]
           for t in range(num_timesteps)]

    # Prepare output buffer
    new_temperature = copy.deepcopy(temperature)
    timestep_durations = []

    # Diffusion loop
    for t in range(num_timesteps):
        start = time.time()
        for d in range(1, depth-1):
            for i in range(1, lat-1):
                for j in range(1, lon-1):
                    if mask[t][d][i][j]:
                        center = temperature[t][d][i][j]
                        total = 0.0
                        count = 0
                        # 6 neighbors
                        for dd, ii, jj in (
                            (d-1,i,j), (d+1,i,j),
                            (d,i-1,j), (d,i+1,j),
                            (d,i,j-1), (d,i,j+1)
                        ):
                            if mask[t][dd][ii][jj]:
                                total += temperature[t][dd][ii][jj]
                                count += 1
                        # apply diffusion
                        if count > 0:
                            delta = diffusion_coeff * (total - count*center) / count
                        else:
                            delta = 0.0
                        new_temperature[t][d][i][j] = center + delta
        timestep_durations.append(time.time() - start)
        # copy new → temperature for next step
        temperature[t] = copy.deepcopy(new_temperature[t])

    # Convert to NumPy array for saving
    final = np.array(new_temperature)

    # Save result
    save_to_netcdf(data, final, DATA_DIR / OUTPUT_FILE_PUREPYTHON, num_timesteps)

    total = sum(timestep_durations)
    avg = total / num_timesteps

    print(f"PurePython model completed in {total:.4f} seconds. "
          f"Average time per timestep: {avg:.4f} seconds.")

def run_diffusion_purepython():
    """
    Entry point for running the pure Python diffusion model via command line.

    Parses --num_timesteps and invokes temperature_diffusion_purepython().
    """
    parser = argparse.ArgumentParser(description="Run 3D Diffusion Model in pure Python")
    parser.add_argument("--num_timesteps", type=int, default=300, help="Number of Timesteps")
    args = parser.parse_args()
    temperature_diffusion_purepython(data=load_data(), num_timesteps=args.num_timesteps)
