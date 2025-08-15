"""
Temperature Diffusion Visualization and Data Utilities

This module provides:
- GPU/CPU hardware queries
- Downloading ocean temperature subsets from Copernicus
- Summary statistics for NetCDF temperature files
- Static 2D surface plots
- Interactive 2D slice animations
- Interactive 3D cube animations

Entry points (via CLI):
- summary()
- visualisation_static()
- visualisation_slice()
- visualisation_cube()
"""

# -------------------------------------------------------------------
# Library imports
# -------------------------------------------------------------------

from ast import Str
from matplotlib import animation
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path
import plotly.graph_objects as go
import argparse
import subprocess
import os
import cupy

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
# Define the root directory
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "model_data"
OUTPUT_DIR = ROOT_DIR / "output"
ORIGINAL_DATA_FILE = "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_thetao_13.83W-6.17E_46.83N-65.25N_0.49-5727.92m_2024-01-01-2024-01-02.nc"

def cuda_check():
    """
    Print the number of available CUDA-capable GPU devices.

    Uses CuPy's runtime API to query device count.
    """
    num_devices = cupy.cuda.runtime.getDeviceCount()
    print(f"Number of CUDA devices: {num_devices}")

def download_ocean_data():
    """
    Download a subset of ocean temperature data using the CopernicusMarine CLI.

    Changes into DATA_DIR, runs 'poetry run copernicusmarine subset' with
    the specified bounding box and time range, then returns to DATA_DIR.

    On success, prints a success message; on failure, prints the error.
    """
    command = [
        "poetry", "run", "copernicusmarine", "subset",
        "--dataset-id", "cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i",
        "--variable", "thetao",
        "--start-datetime", "2024-01-01T00:00:00",
        "--end-datetime", "2024-01-02T00:00:00",
        "--minimum-longitude", "-13.903248235212025",
        "--maximum-longitude", "6.186015157645116",
        "--minimum-latitude", "46.82995633719309",
        "--maximum-latitude", "65.31207865862164",
        "--minimum-depth", "0.49402499198913574",
        "--maximum-depth", "5727.9169921875"
    ]

    os.chdir(DATA_DIR)
    
    try:
        # Run the command and enable interactive mode by attaching directly to the terminal's stdin/stdout
        result = subprocess.run(command, check=True)
        print("Data downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
    finally:
        # Change back to the original directory
        os.chdir(DATA_DIR)

def calculate_summary(data_file):
    """
    Load a NetCDF file and print summary statistics for 'thetao'.

    Args:
        data_file (str): Filename (within DATA_DIR) of the .nc dataset.

    Prints:
        - Array shape (time, depth, lat, lon)
        - Mean, max, min, std of the temperature
        - Full dataset dimension and coordinate details
    """
    # Load the NetCDF file from the data directory
    file_path = DATA_DIR / data_file
    data = xr.open_dataset(file_path)
    
    # Assume the variable of interest is named 'temperature' (check the variable name in your file)
    temperature = data['thetao']
    print("The dimensions of the data is: " + str(temperature.shape))
    # Print some summary statistics
    print("Temperature Summary Statistics:")
    print("Mean temperature:", temperature.mean().item())
    print("Max temperature:", temperature.max().item())
    print("Min temperature:", temperature.min().item())
    print("Standard deviation:", temperature.std().item())

    # Optional: Print information about dimensions and coordinates
    print("\nDataset Dimensions and Coordinates:")
    print(data)

def summary():
    """
    CLI entry point for calculate_summary.

    Usage:
        python this_script.py --data-file filename.nc
    """
    parser = argparse.ArgumentParser(description="Calculate Summary Statistics for a datafile")
    parser.add_argument("--data-file", type=str, default=ORIGINAL_DATA_FILE, help="Data file for visualisation.")

    args = parser.parse_args()

    # Pass parsed arguments to visualisation_slice
    calculate_summary(data_file=args.data_file)

def visualisation_static():
    """
    CLI entry point for generating a static 2D surface plot of temperature.

    Produces a PNG of the surface (time=0, depth=0) saved in OUTPUT_DIR.
    """
    parser = argparse.ArgumentParser(
        description="Generate a static 2D temperature slice"
    )
    parser.add_argument(
        "--data-file", "-f",
        default=ORIGINAL_DATA_FILE,
        help="Which .nc file to visualize"
    )
    args = parser.parse_args()

    # Now call your existing logic, passing args.data_file
    file_path = DATA_DIR / args.data_file
    data = xr.open_dataset(file_path)
    theta = data["thetao"].isel(time=0, depth=0)
    lats = theta["latitude"].values
    lons = theta["longitude"].values

    fig, ax = plt.subplots(figsize=(10, 6))
    c = ax.pcolormesh(lons, lats, theta.values, shading="auto", cmap="viridis")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title(f"Surface Temperature: {args.data_file}")
    fig.colorbar(c, ax=ax, label="°C")

    save_path = OUTPUT_DIR / f"{Path(args.data_file).stem}_static.png"
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved to {save_path}")


def plot_slice(target_depth=0, animation_speed=100, data_file=ORIGINAL_DATA_FILE):
    """
    Create an interactive 2D heatmap animation over time at a given depth.

    Args:
        target_depth (float): Desired depth in metres.
        animation_speed (int): Frame duration in milliseconds.
        data_file (str): NetCDF filename in DATA_DIR.

    Saves:
        An HTML file with a Plotly animated heatmap in OUTPUT_DIR.
    """
    # Load the NetCDF file
    file_path = DATA_DIR / data_file
    data = xr.open_dataset(file_path)

    # Assume the variable of interest is named 'temperature' (check the variable name in your file)
    temperature = data['thetao']

    # Find the closest depth level to the target depth
    depths = temperature['depth'].values
    closest_depth_idx = (abs(depths - target_depth)).argmin()
    selected_depth = depths[closest_depth_idx]
    temperature_subset = temperature.isel(depth=closest_depth_idx)
    # Calculate the max temperature value across the subset for setting the color scale
    # Calculate the max and min temperature values across the subset, ignoring NaNs
    max_temp = np.nanmax(temperature_subset.values)
    min_temp = np.nanmin(temperature_subset.values)

    print("MAX TEMP: " + str(max_temp))
    print("MIN TEMP: " + str(min_temp))

    print("The depth being visualised is: " + str(selected_depth) + " as the target depth inputted was: " + str(target_depth))

    # Prepare latitudes, longitudes, and time steps
    latitudes = temperature['latitude'].values
    longitudes = temperature['longitude'].values
    time_steps = temperature['time'].values
    
    # Create the figure and initial heatmap for the first time step
    fig = go.Figure(data=go.Heatmap(
        z=temperature_subset.isel(time=0).values,
        x=longitudes,
        y=latitudes,
        colorscale='Viridis',
        colorbar=dict(title='Temperature (°C)'),
        zmin=min_temp,  # Set color range minimum
        zmax=max_temp    # Set color range maximum

    ))

    # Define frames for each time step
    frames = []
    for t in range(len(time_steps)):
        frames.append(go.Frame(
            data=[go.Heatmap(
                z=temperature_subset.isel(time=t).values,
                x=longitudes,
                y=latitudes,
                colorscale='Viridis',
                zmin=min_temp,  # Set color range minimum
                zmax=max_temp    # Set color range maximum
            )],
            name=f"Time {t}"
        ))

    fig.frames = frames

    # Add slider and play button to animate over all time steps
    fig.update_layout(
        title=f"Ocean Temperature Slice at Depth Level {selected_depth}m (Closest to {target_depth}m)",
        xaxis_title="Longitude",
        yaxis_title="Latitude",
        updatemenus=[{
            "type": "buttons",
            "showactive": False,
            "buttons": [{
                "label": "Play",
                "method": "animate",
                "args": [None, {"frame": {"duration": animation_speed, "redraw": True}, "fromcurrent": True}]  # Adjust duration here
            }, {
                "label": "Pause",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}]
            }]
        }],
        sliders=[{
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Time Step: ",
                "visible": True,
                "xanchor": "right"
            },
            "steps": [{
                "label": f"{t}",
                "method": "animate",
                "args": [[f"Time {t}"], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}]  # Adjust duration here
            } for t in range(len(time_steps))]
        }]
    )

    # Save the interactive plot as an HTML file
    if data_file==ORIGINAL_DATA_FILE:
        save_path = OUTPUT_DIR / "original_temperature_2d_interactive.html"
    else:
        save_path = OUTPUT_DIR / "predicted_temperature_2d_interactive.html"

    fig.write_html(save_path)

def visualisation_slice():
    """
    CLI entry point for the 2D interactive slice animation.

    Usage:
        python this_script.py --target_depth 50 --animation_speed 300 --data-file file.nc
    """
    parser = argparse.ArgumentParser(
        description="Animate a 2D temperature slice over time"
    )
    parser.add_argument("--target_depth",   type=int, default=50,  help="Depth in metres")
    parser.add_argument("--animation_speed",type=int, default=300, help="ms per frame")
    parser.add_argument(
        "--data-file", "-f",
        default=ORIGINAL_DATA_FILE,
        help="Which .nc file to visualize"
    )
    args = parser.parse_args()

    plot_slice(
        target_depth=args.target_depth,
        animation_speed=args.animation_speed,
        data_file=args.data_file
    )




def plot_cube(num_depths=3, num_time_steps=3, data_file=ORIGINAL_DATA_FILE):
    """
    Create an interactive 3D surface animation over time and depth.

    Args:
        num_depths (int): Number of depth levels to include.
        num_time_steps (int): Number of time frames to animate.
        data_file (str): NetCDF filename in DATA_DIR.

    Saves:
        An HTML file with a Plotly 3D animated cube in OUTPUT_DIR.
    """
    # Load the NetCDF file
    file_path = DATA_DIR / data_file
    data = xr.open_dataset(file_path)

    # Assume the variable of interest is named 'temperature' (check the variable name in your file)
    temperature = data['thetao']

    # Prepare data for 3D plotting (take the specified number of depth and time levels)
    latitudes = temperature['latitude'].values
    longitudes = temperature['longitude'].values
    depths = temperature['depth'].values[:num_depths]
    time_steps = temperature['time'].values[:num_time_steps]
    temperature_values = temperature.isel(depth=slice(0, num_depths), time=slice(0, num_time_steps)).values

    # Calculate the max temperature value across the subset for setting the color scale
    # Calculate the max and min temperature values across the subset, ignoring NaNs
    max_temp = np.nanmax(temperature_values)
    min_temp = np.nanmin(temperature_values)

    print("MAX TEMP: " + str(max_temp))
    print("MIN TEMP: " + str(min_temp))

    # Create the figure and define frames for each time step
    fig = go.Figure()

    # Create initial frame (first time step)
    for i, depth in enumerate(depths):
        fig.add_trace(go.Surface(
            z=[[depth] * len(longitudes) for _ in range(len(latitudes))],
            x=longitudes,
            y=latitudes,
            surfacecolor=temperature_values[0, i],
            colorscale='Viridis',
            colorbar=dict(title='Temperature (°C)'),
            zmin=min_temp,  # Set color range minimum
            zmax=max_temp    # Set color range maximum
        ))

    # Define frames for each subsequent time step
    frames = []
    for t, time in enumerate(time_steps):
        frame_data = []
        for i, depth in enumerate(depths):
            frame_data.append(go.Surface(
                z=[[depth] * len(longitudes) for _ in range(len(latitudes))],
                x=longitudes,
                y=latitudes,
                surfacecolor=temperature_values[t, i],
                colorscale='Viridis',
                zmin=min_temp,  # Set color range minimum
                zmax=max_temp    # Set color range maximum
            ))
        frames.append(go.Frame(data=frame_data, name=f"Time {t}"))

    fig.frames = frames

    # Set up play button and slider
    fig.update_layout(
        title="3D Ocean Temperature Profile Over Time",
        scene=dict(
            xaxis_title="Longitude",
            yaxis_title="Latitude",
            zaxis_title="Depth (m)",
            zaxis=dict(autorange="reversed")
        ),
        updatemenus=[{
            "type": "buttons",
            "showactive": False,
            "buttons": [{
                "label": "Play",
                "method": "animate",
                "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
            }, {
                "label": "Pause",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}]
            }]
        }],
        sliders=[{
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Time Step: ",
                "visible": True,
                "xanchor": "right"
            },
            "steps": [{
                "label": f"{t}",
                "method": "animate",
                "args": [[f"Time {t}"], {"frame": {"duration": 500, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}]
            } for t in range(len(time_steps))]
        }]
    )

    # Save the interactive plot as an HTML file
    # Save the interactive plot as an HTML file
    if data_file==ORIGINAL_DATA_FILE:
        save_path = OUTPUT_DIR / "original_temperature_3d_interactive.html"
    else:
        save_path = OUTPUT_DIR / "predicted_temperature_3d_interactive.html"
    fig.write_html(save_path)

def visualisation_cube():
    """
    CLI entry point for the 3D cube animation.

    Usage:
        python this_script.py --num_depths 5 --num_time_steps 3 --data-file file.nc
    """
    parser = argparse.ArgumentParser(
        description="Animate a 3D temperature cube over time"
    )
    parser.add_argument("--num_depths",     type=int, default=5, help="Number of depth levels")
    parser.add_argument("--num_time_steps", type=int, default=3, help="Number of time steps")
    parser.add_argument(
        "--data-file", "-f",
        default=ORIGINAL_DATA_FILE,
        help="Which .nc file to visualize"
    )
    args = parser.parse_args()

    plot_cube(
        num_depths=args.num_depths,
        num_time_steps=args.num_time_steps,
        data_file=args.data_file
    )



