"""
Temperature Diffusion Experiment Runner

This script benchmarks three implementations of a 3D temperature diffusion model:
- Pure Python nested loops
- NumPy (CPU)
- CuPy (GPU)

It records timing results over multiple timesteps and repeats, saves them to CSV,
and generates an error‐bar plot comparing performance across methods.

Functions:
- get_gpu_name: Query the GPU model via nvidia‐smi.
- get_cpu_name: Read the CPU model string from /proc/cpuinfo.
- plot_timings: Read the CSV of results and produce an error‐bar plot.
"""

# -------------------------------------------------------------------
# Library imports
# -------------------------------------------------------------------

import subprocess
import time
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------

# ensure directory for outputs
OUT_DIR = "../output"
os.makedirs(OUT_DIR, exist_ok=True)

def get_gpu_name():
    """
    Query the system GPU name using `nvidia-smi`.

    Returns:
        str: The name of the first GPU, or "Unknown GPU" if the command fails.
    """
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            stderr=subprocess.DEVNULL
        ).decode().strip().splitlines()
        return out[0]
    except Exception:
        return "Unknown GPU"

def get_cpu_name():
    """
    Read the CPU model name from /proc/cpuinfo (Linux).

    Returns:
        str: The CPU model string, or "Unknown CPU" if reading fails.
    """
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.lower().startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except:
        pass
    return "Unknown CPU"

def plot_timings(csv_filename):
    """
    Read benchmarking CSV and create an error‐bar plot of runtimes.

    The CSV must have columns:
      method, num_timesteps, mean_time_sec, std_dev_sec

    X‐axis: number of timesteps
    Y‐axis: mean runtime in seconds, with error bars showing standard deviation

    Args:
        csv_filename (str): Path to the CSV file of timing results.
    """

    data = {}
    timesteps = []
    with open(csv_filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            method = row["method"]
            ts = int(row["num_timesteps"])
            mean_t = float(row["mean_time_sec"])
            std_t  = float(row["std_dev_sec"])
            data.setdefault(method, []).append((ts, mean_t, std_t))
            if ts not in timesteps:
                timesteps.append(ts)

    timesteps = sorted(timesteps)
    plt.figure()
    for method, vals in data.items():
        # sort vals by ts
        vals = sorted(vals, key=lambda x: x[0])
        xs = [v[0] for v in vals]
        ys = [v[1] for v in vals]
        errs = [v[2] for v in vals]
        plt.errorbar(xs, ys, yerr=errs, label=method, marker='o')

    plt.xlabel("Number of timesteps")
    plt.ylabel("Time (s)")
    plt.title("Temperature Diffusion Performance")
    plt.legend()
    png = os.path.join(OUT_DIR, "temperature_diffusion_timings.png")
    plt.savefig(png)
    plt.close()
    print(f"Plot saved to {png}")

if __name__ == "__main__":
    """
    Main execution block:

    1. Detect hardware (GPU, CPU).
    2. Define which diffusion scripts to run.
    3. Loop over methods, timesteps, and repeats:
       - Run each script via subprocess.
       - Measure elapsed time.
       - Record results to CSV.
    4. After all runs, generate an error‐bar plot.
    """

    gpu_name = get_gpu_name()
    cpu_name = get_cpu_name()

    # map display names → console_script names
    methods = {
        "Pure Python": "diffusion_pure_python",
        "NumPy (CPU)": "diffusion_numpy",
        "CuPy (GPU)": "diffusion_cupy",
    }

    #timesteps_list = [10, 25, 50, 100]
    timesteps_list = [3]
    repeats = 3

    csv_file = os.path.join(OUT_DIR, "temperature_diffusion_timings.csv")
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "gpu_name", "cpu_name",
            "method", "num_timesteps",
            "mean_time_sec", "std_dev_sec"
        ])

        for method, script in methods.items():
            for ts in timesteps_list:
                times = []
                for _ in range(repeats):
                    start = time.time()
                    subprocess.check_call([script, f"--num_timesteps={ts}"])
                    times.append(time.time() - start)
                writer.writerow([
                    gpu_name, cpu_name,
                    method, ts,
                    f"{np.mean(times):.6f}",
                    f"{np.std(times):.6f}"
                ])
                print(f"{method}, ts={ts}: mean {np.mean(times):.4f}s, std {np.std(times):.4f}s")

    print(f"CSV timings saved to {csv_file}")
    plot_timings(csv_file)
