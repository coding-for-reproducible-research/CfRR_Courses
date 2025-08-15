"""
Game of Life Profiling Suite

This script augments the Game of Life implementations (NumPy, CuPy, Naive)
with profiling instrumentation, allowing you to collect CPU profiles via
cProfile/pstats and GPU NVTX ranges via CuPy’s profiler and time_range
decorator.

Entry points (via CLI):
- run_life_numpy(): NumPy backend, optional --profile-cpu
- run_life_cupy():  CuPy backend, optional --profile-cpu, --profile-gpu
- run_life_naive(): Naive Python backend, optional --profile-cpu
"""
# -------------------------------------------------------------------
# Library imports
# -------------------------------------------------------------------
import argparse
import cProfile
import pstats
from pathlib import Path
import numpy as np
import cupy as cp
from cupyx.profiler import time_range
from cupy.cuda import profiler
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ─────────────────────────────────────────────────────────────────────────────
# 1) Core update functions (decorated with NVTX ranges via cupyx.profiler)
# ─────────────────────────────────────────────────────────────────────────────
@time_range()
def life_step_numpy(grid: np.ndarray) -> np.ndarray:
    """
    Next-generation update using NumPy with NVTX profiling.

    Applies the 8-neighbor Conway’s Game of Life rules on a toroidal grid.

    Args:
        grid (np.ndarray): 2D array of 0s and 1s.

    Returns:
        np.ndarray: Updated 2D array for the next generation.
    """
    neighbours = (
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1) +
        np.roll(grid, 1, axis=0) +
        np.roll(grid, -1, axis=0) +
        np.roll(grid, 1, axis=1) +
        np.roll(grid, -1, axis=1)
    )
    return np.where((neighbours == 3) | ((grid == 1) & (neighbours == 2)), 1, 0)

@time_range()
def life_step_gpu(grid: cp.ndarray) -> cp.ndarray:
    """
    Next-generation update using CuPy with NVTX profiling.

    Identical logic to life_step_numpy, but leverages GPU arrays.

    Args:
        grid (cp.ndarray): 2D CuPy array of 0s and 1s.

    Returns:
        cp.ndarray: Updated 2D CuPy array.
    """
    neighbours = (
        cp.roll(cp.roll(grid, 1, axis=0), 1, axis=1) +
        cp.roll(cp.roll(grid, 1, axis=0), -1, axis=1) +
        cp.roll(cp.roll(grid, -1, axis=0), 1, axis=1) +
        cp.roll(cp.roll(grid, -1, axis=0), -1, axis=1) +
        cp.roll(grid, 1, axis=0) +
        cp.roll(grid, -1, axis=0) +
        cp.roll(grid, 1, axis=1) +
        cp.roll(grid, -1, axis=1)
    )
    return cp.where((neighbours == 3) | ((grid == 1) & (neighbours == 2)), 1, 0)

@time_range()
def life_step_naive(grid: np.ndarray) -> np.ndarray:
    """
    Next-generation update with a naive Python loop and NVTX profiling.

    Iterates over each cell and its 8 neighbors on a toroidal grid.

    Args:
        grid (np.ndarray): 2D array of 0s and 1s.

    Returns:
        np.ndarray: Updated 2D array.
    """
    N, M = grid.shape
    new = np.zeros((N, M), dtype=int)
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = (i + di) % N, (j + dj) % M
                    cnt += grid[ni, nj]
            if grid[i, j] == 1:
                new[i, j] = 1 if cnt in (2, 3) else 0
            else:
                new[i, j] = 1 if cnt == 3 else 0
    return new

# -------------------------------------------------------------------
# 2) Simulation loops (also bracketed with NVTX ranges)
# -------------------------------------------------------------------
@time_range()
def simulate_life_numpy(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run Game of Life for NumPy with NVTX profiling of the loop.

    Args:
        N (int): Grid dimension (N × N).
        timesteps (int): Number of generations.
        p_alive (float): Initial probability of being alive.
        record_history (bool): If True, collect each generation in a list.

    Returns:
        list[np.ndarray] or None: Generation history if recorded, else None.
    """
    grid = np.random.choice([0, 1], size=(N, N), p=[1 - p_alive, p_alive])
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(grid.copy())
        grid = life_step_numpy(grid)
    return history

@time_range()
def simulate_life_cupy(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run Game of Life on GPU with NVTX profiling of the loop.

    Args:
        N (int): Grid size.
        timesteps (int): Number of generations.
        p_alive (float): Initial alive probability.
        record_history (bool): If True, store each generation as NumPy array.

    Returns:
        list[np.ndarray] or None: Recorded history if requested.
    """
    grid_gpu = (cp.random.random((N, N)) < p_alive).astype(cp.int32)
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(cp.asnumpy(grid_gpu))
        grid_gpu = life_step_gpu(grid_gpu)
    return history

@time_range()
def simulate_life_naive(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run naive Python Game of Life with NVTX profiling of the loop.

    Args:
        N (int): Grid size.
        timesteps (int): Number of generations.
        p_alive (float): Initial alive probability.
        record_history (bool): If True, collect each generation.

    Returns:
        list[np.ndarray] or None: History of grids if recorded.
    """
    grid = np.random.choice([0, 1], size=(N, N), p=[1 - p_alive, p_alive])
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(grid.copy())
        grid = life_step_naive(grid)
    return history

# ─────────────────────────────────────────────────────────────────────────────
# 3) Animation/export (unchanged)
# ─────────────────────────────────────────────────────────────────────────────
def animate_life(history, output_file: Path, interval: int = 200, dpi: int = 80):
    """
    Create and save a GIF of the simulation history.

    Args:
        history (list[np.ndarray]): Recorded generations to animate.
        output_file (Path): Filepath for the output GIF.
        interval (int): Delay between frames in milliseconds.
        dpi (int): Dots per inch resolution for the saved GIF.
    """
    

    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(history[0], cmap='binary')
    ax.set_axis_off()

    def _update(idx):
        im.set_data(history[idx])
        return [im]

    anim = animation.FuncAnimation(
        fig, _update,
        frames=len(history),
        interval=interval,
        blit=True
    )
    anim.save(str(output_file), writer='pillow', dpi=dpi)
    plt.close(fig)

# ─────────────────────────────────────────────────────────────────────────────
# 4) CLI entry-points
# ─────────────────────────────────────────────────────────────────────────────
def run_life_numpy():
    """
    CLI for NumPy Game of Life with optional CPU profiling.

    Flags:
      --size:        Grid dimension (N×N)
      --timesteps:   Number of generations
      --save-gif:    Save a GIF if size ≤ 100
      --profile-cpu: Enable cProfile CPU profiling
    """
    p = argparse.ArgumentParser("Game of Life (NumPy)")
    p.add_argument("--size",      type=int, default=100)
    p.add_argument("--timesteps", type=int, default=50)
    p.add_argument("--save-gif",  action="store_true")
    p.add_argument("--profile-cpu", action="store_true")
    args = p.parse_args()

    # CPU profiling
    if args.profile_cpu:
        pr = cProfile.Profile()
        pr.enable()

    history = simulate_life_numpy(args.size, args.timesteps, record_history=args.save_gif)

    if args.save_gif and args.size <= 100:
        out = Path("game_of_life_cpu.gif")
        animate_life(history, out)
        print(f"Saved CPU GIF to {out}")

    if args.profile_cpu:
        pr.disable()
        stats = pstats.Stats(pr).strip_dirs().sort_stats("cumtime")
        stats.print_stats(20)

def run_life_cupy():
    """
    CLI for CuPy Game of Life with optional CPU/GPU profiling.

    Flags:
      --size:        Grid dimension (N×N)
      --timesteps:   Number of generations
      --save-gif:    Save a GIF if size ≤ 100
      --profile-cpu: Enable cProfile CPU profiling
      --profile-gpu: Enable NVIDIA CUPTI GPU profiling
    """
    p = argparse.ArgumentParser("Game of Life (CuPy)")
    p.add_argument("--size",      type=int, default=100)
    p.add_argument("--timesteps", type=int, default=50)
    p.add_argument("--save-gif",  action="store_true")
    p.add_argument("--profile-cpu", action="store_true")
    p.add_argument("--profile-gpu", action="store_true")
    args = p.parse_args()

    # CPU profiling
    if args.profile_cpu:
        pr = cProfile.Profile()
        pr.enable()

    # CUPTI profiling
    if args.profile_gpu:
        profiler.start()

    history = simulate_life_cupy(args.size, args.timesteps, record_history=args.save_gif)

    if args.save_gif and args.size <= 100:
        out = Path("game_of_life_gpu.gif")
        animate_life(history, out)
        print(f"Saved GPU GIF to {out}")

    if args.profile_gpu:
        profiler.stop()

    if args.profile_cpu:
        pr.disable()
        stats = pstats.Stats(pr).strip_dirs().sort_stats("cumtime")
        stats.print_stats(20)

def run_life_naive():
    """
    CLI for Naive Python Game of Life with optional CPU profiling.

    Flags:
      --size:        Grid dimension (N×N)
      --timesteps:   Number of generations
      --save-gif:    Save a GIF if size ≤ 100
      --profile-cpu: Enable cProfile CPU profiling
    """
    p = argparse.ArgumentParser("Game of Life (Naive)")
    p.add_argument("--size",      type=int, default=100)
    p.add_argument("--timesteps", type=int, default=50)
    p.add_argument("--save-gif",  action="store_true")
    p.add_argument("--profile-cpu", action="store_true")
    args = p.parse_args()

    if args.profile_cpu:
        pr = cProfile.Profile()
        pr.enable()

    history = simulate_life_naive(args.size, args.timesteps, record_history=args.save_gif)

    if args.save_gif and args.size <= 100:
        out = Path("game_of_life_naive.gif")
        animate_life(history, out)
        print(f"Saved Naive GIF to {out}")

    if args.profile_cpu:
        pr.disable()
        stats = pstats.Stats(pr).strip_dirs().sort_stats("cumtime")
        stats.print_stats(20)
