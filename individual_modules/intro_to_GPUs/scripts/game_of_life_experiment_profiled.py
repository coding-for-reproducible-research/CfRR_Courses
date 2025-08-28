"""
Benchmarking Suite for Profiled Game of Life Implementations

This script runs profiled entry-points for three versions of Conway’s Game of Life:
  - NumPy (CPU):     game_of_life_cpu_profiled
  - CuPy (GPU):      game_of_life_gpu_profiled
  - Naive (CPU):     game_of_life_naive_profiled

For each combination of grid size and timestep count, it:
  1. Executes each implementation multiple times via Poetry entry-points.
  2. Computes mean and standard deviation of run times.
  3. Writes results to a CSV file.
  4. Generates an error-bar plot (execution time vs. grid size) saved alongside the CSV.
"""

# ─────────────────────────────────────────────────────────────────────────────
# Library imports
# ─────────────────────────────────────────────────────────────────────────────

import subprocess
import time
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

# Ensure output directory exists
out_dir = "../output"
os.makedirs(out_dir, exist_ok=True)

def get_gpu_name():
    """
    Query the GPU model name via `nvidia-smi`.

    Returns:
        str: The first GPU’s name, or 'Unknown_GPU' if detection fails.
    """
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            stderr=subprocess.DEVNULL
        ).decode().strip().splitlines()
        return out[0]
    except Exception:
        return "Unknown_GPU"

def get_cpu_name():
    """
    Query the CPU model name via `lscpu` on Linux.

    Returns:
        str: The CPU model string, or 'Unknown_CPU' if detection fails.
    """
    try:
        out = subprocess.check_output(["lscpu"], stderr=subprocess.DEVNULL).decode().splitlines()
        for line in out:
            if line.startswith("Model name:"):
                return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return "Unknown_CPU"

def plot_timings(csv_filename):
    """
    Read benchmark CSV and generate an error-bar plot of runtime vs grid size.

    The CSV must include columns:
        gpu, cpu, method, grid_size, timesteps, mean_time_sec, std_dev_sec

    Args:
        csv_filename (Path): Path to the CSV file of timing results.
    """
    data = {}
    timesteps = None
    with open(csv_filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            method = row["method"]
            size = int(row["grid_size"])
            mean_t = float(row["mean_time_sec"])
            std_t = float(row["std_dev_sec"])
            timesteps = row["timesteps"]
            data.setdefault(method, {"sizes": [], "means": [], "stds": []})
            data[method]["sizes"].append(size)
            data[method]["means"].append(mean_t)
            data[method]["stds"].append(std_t)

    plt.figure(figsize=(10, 6))
    for method, vals in data.items():
        plt.errorbar(
            vals["sizes"],
            vals["means"],
            yerr=vals["stds"],
            label=method,
            marker="o",
            capsize=5
        )
    plt.title(f"Game of Life - Time vs Grid Size (Timesteps = {timesteps})")
    plt.xlabel("Grid Size (N x N)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save PNG next to CSV
    base = os.path.splitext(os.path.basename(csv_filename))[0]
    out_png = os.path.join(os.path.dirname(csv_filename), f"{base}.png")
    plt.savefig(out_png, dpi=300)
    plt.close()
    print(f"Saved plot: {out_png}")



# ─────────────────────────────────────────────────────────────────────────────
# Main benchmarking loop
# ─────────────────────────────────────────────────────────────────────────────

def run_experiment():
    """
    Main benchmarking routine.

    Detects hardware names, defines profiled entry-points, loops over grid sizes
    and timesteps, records timing statistics to CSV, and generates plots.
    """

    gpu_name = get_gpu_name().replace(" ", "_")
    cpu_name = get_cpu_name().replace(" ", "_")

    # Updated to use the profiled entry-points defined in pyproject.toml:
    methods = {
        "NumPy (CPU)": "game_of_life_cpu_profiled",
        "CuPy (GPU)":  "game_of_life_gpu_profiled",
        "Naive (CPU)": "game_of_life_naive_profiled",
    }

    # Strip off both the "game_of_life_" prefix and the "_profiled" suffix
    clean_names = [
        v.replace("game_of_life_", "").replace("_profiled", "")
        for v in methods.values()
    ]
    method_ids = "_".join(sorted(clean_names))

    #grid_sizes     = [50, 100, 250, 500, 1000]
    grid_sizes     = [10, 25, 50, 100]
    timesteps_list = [100]
    repeats        = 3

    for timesteps in timesteps_list:
        # Filename now includes GPU, CPU, all methods, and timesteps
        csv_filename = os.path.join(
            out_dir,
            f"gol_timings_{gpu_name}_{cpu_name}_{method_ids}_ts{timesteps}.csv"
        )

        with open(csv_filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "gpu", "cpu", "method",
                "grid_size", "timesteps",
                "mean_time_sec", "std_dev_sec"
            ])

            print(f"\n==== Running benchmarks for {timesteps} timesteps ====")
            for size in grid_sizes:
                for method_name, entry_point in methods.items():
                    run_times = []
                    for i in range(repeats):
                        cmd = [
                            "poetry", "run", entry_point,
                            "--size", str(size),
                            "--timesteps", str(timesteps)
                        ]
                        print(f"  {method_name:<12} | {size:6}×{size:<6} | run {i+1}/{repeats}")
                        t0 = time.perf_counter()
                        subprocess.run(cmd, check=True)
                        t1 = time.perf_counter()
                        run_times.append(t1 - t0)

                    mean_t = np.mean(run_times)
                    std_t  = np.std(run_times)
                    writer.writerow([
                        gpu_name, cpu_name,
                        method_name,
                        size, timesteps,
                        f"{mean_t:.6f}",
                        f"{std_t:.6f}"
                    ])

        print(f"Saved CSV: {csv_filename}")

        # Generate the plot from that CSV
        plot_timings(csv_filename)
