"""
Conway’s Game of Life Simulation

This module implements core update rules and simulation drivers for Conway’s
Game of Life on 2D grids, with three backends:
- NumPy vectorized updates
- CuPy GPU-accelerated updates
- Naive Python nested loops

It also provides an animation exporter (GIF via matplotlib) and CLI entry points:
- run_life_numpy()
- run_life_cupy()
- run_life_naive()
"""

# -------------------------------------------------------------------
# Library imports
# -------------------------------------------------------------------
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cupy as cp


# ─────────────────────────────────────────────────────────────────────────────
# 1) Core update functions (no plotting/animation)
# ─────────────────────────────────────────────────────────────────────────────

def life_step_numpy(grid: np.ndarray) -> np.ndarray:
    """
    Compute the next generation of the Game of Life using NumPy.

    Applies the standard 8‐neighbor Conway rules on a toroidal grid:
      - A dead cell with exactly 3 neighbors becomes alive.
      - A live cell with 2 or 3 neighbors stays alive.
      - Otherwise, the cell dies or remains dead.

    Args:
        grid (np.ndarray): 2D array of 0s and 1s representing the current state.

    Returns:
        np.ndarray: 2D array of the same shape for the next generation.
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


def life_step_gpu(grid: cp.ndarray) -> cp.ndarray:
    """
    Compute the next generation of the Game of Life using CuPy on GPU.

    Identical rules to life_step_numpy, but leverages GPU arrays.

    Args:
        grid (cp.ndarray): 2D CuPy array of 0s and 1s.

    Returns:
        cp.ndarray: Next-generation 2D CuPy array.
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


def life_step_naive(grid: np.ndarray) -> np.ndarray:
    """
    Compute the next generation with a naive Python loop implementation.

    Iterates over each cell and its 8 neighbors, applying wrap-around.

    Args:
        grid (np.ndarray): 2D array of 0s and 1s.

    Returns:
        np.ndarray: Next-generation 2D array.
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
                new[i, j] = 1 if (cnt == 2 or cnt == 3) else 0
            else:
                new[i, j] = 1 if (cnt == 3) else 0
    return new


# ─────────────────────────────────────────────────────────────────────────────
# 2) Simulation functions (no animation)
# ─────────────────────────────────────────────────────────────────────────────

def simulate_life_numpy(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run a Game of Life simulation using the NumPy backend.

    Initializes a random NxN grid with alive probability p_alive,
    then iterates the specified number of timesteps.

    Args:
        N (int): Grid dimension (N × N).
        timesteps (int): Number of generations to simulate.
        p_alive (float): Probability that a cell starts alive.
        record_history (bool): If True, collect each generation in a list.

    Returns:
        list[np.ndarray] or None: History of grids if record_history else None.
    """
    grid = np.random.choice([0, 1], size=(N, N), p=[1 - p_alive, p_alive])
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(grid.copy())
        grid = life_step_numpy(grid)
    return history


def simulate_life_cupy(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run a Game of Life simulation on GPU using CuPy.

    Args:
        N (int): Grid dimension (N × N).
        timesteps (int): Number of generations.
        p_alive (float): Initial alive probability.
        record_history (bool): If True, collect grids (converted to NumPy).

    Returns:
        list[np.ndarray] or None: History of grids as NumPy arrays if recorded.
    """
    grid_gpu = (cp.random.random((N, N)) < p_alive).astype(cp.int32)
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(cp.asnumpy(grid_gpu))
        grid_gpu = life_step_gpu(grid_gpu)
    return history


def simulate_life_naive(N: int, timesteps: int, p_alive: float = 0.2, record_history: bool = False):
    """
    Run a Game of Life simulation with the naive Python implementation.

    Args:
        N (int): Grid size.
        timesteps (int): Number of generations.
        p_alive (float): Starting alive probability.
        record_history (bool): Whether to collect each generation.

    Returns:
        list[np.ndarray] or None: Recorded history if requested.
    """
    grid = np.random.choice([0, 1], size=(N, N), p=[1 - p_alive, p_alive])
    history = [] if record_history else None
    for _ in range(timesteps):
        if record_history:
            history.append(grid.copy())
        grid = life_step_naive(grid)
    return history


# ─────────────────────────────────────────────────────────────────────────────
# 3) Animation/export
# ─────────────────────────────────────────────────────────────────────────────

def animate_life(history, output_file: Path, interval: int = 200, dpi: int = 80):
    """
    Create and save a GIF animation of the Game of Life history.

    Uses matplotlib’s FuncAnimation and the pillow writer.

    Args:
        history (list[np.ndarray]): List of 2D grids to animate.
        output_file (Path): Path for the output GIF file.
        interval (int): Delay between frames in ms.
        dpi (int): Resolution of the saved animation.
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
# 4) CLI entry-points (only --size, --timesteps, --save-gif)
# ─────────────────────────────────────────────────────────────────────────────

def run_life_numpy():
    """
    Command‐line entry for NumPy-based Game of Life.

    Parses --size, --timesteps, and --save-gif; runs simulation and optionally saves GIF.
    """
    p = argparse.ArgumentParser("Game of Life (NumPy)")
    p.add_argument("--size",      type=int, default=100, help="Grid dimension (N×N)")
    p.add_argument("--timesteps", type=int, default=50,  help="Number of generations")
    p.add_argument("--save-gif",  action="store_true",   help="Save GIF animation")
    args = p.parse_args()

    print(f"[NumPy] Args received: {args}")
    record = args.save_gif and args.size <= 100
    history = simulate_life_numpy(args.size, args.timesteps, record_history=record)

    if args.save_gif:
        if record:
            output = Path("game_of_life_cpu.gif")
            animate_life(history, output)
            print(f"Saved CPU GIF to {output}")
        else:
            print("[NumPy] Problem size > 100: cannot save history or create GIF.")
    else:
        print("[NumPy] GIF creation skipped; history not saved.")


def run_life_cupy():
    """
    Command‐line entry for CuPy-based Game of Life.

    Same arguments as run_life_numpy, but runs on GPU.
    """
    p = argparse.ArgumentParser("Game of Life (CuPy)")
    p.add_argument("--size",      type=int, default=100, help="Grid dimension (N×N)")
    p.add_argument("--timesteps", type=int, default=50,  help="Number of generations")
    p.add_argument("--save-gif",  action="store_true",   help="Save GIF animation")
    args = p.parse_args()

    print(f"[CuPy] Args received: {args}")
    record = args.save_gif and args.size <= 100
    history = simulate_life_cupy(args.size, args.timesteps, record_history=record)

    if args.save_gif:
        if record:
            output = Path("game_of_life_gpu.gif")
            animate_life(history, output)
            print(f"Saved GPU GIF to {output}")
        else:
            print("[CuPy] Problem size > 100: cannot save history or create GIF.")
    else:
        print("[CuPy] GIF creation skipped; history not saved.")


def run_life_naive():
    """
    Command‐line entry for the naive Python Game of Life.

    Same CLI interface, uses the nested-loop implementation.
    """
    p = argparse.ArgumentParser("Game of Life (Naive)")
    p.add_argument("--size",      type=int, default=100, help="Grid dimension (N×N)")
    p.add_argument("--timesteps", type=int, default=50,  help="Number of generations")
    p.add_argument("--save-gif",  action="store_true",   help="Save GIF animation")
    args = p.parse_args()

    print(f"[Naive] Args received: {args}")
    record = args.save_gif and args.size <= 100
    history = simulate_life_naive(args.size, args.timesteps, record_history=record)

    if args.save_gif:
        if record:
            output = Path("game_of_life_naive.gif")
            animate_life(history, output)
            print(f"Saved Naive GIF to {output}")
        else:
            print("[Naive] Problem size > 100: cannot save history or create GIF.")
    else:
        print("[Naive] GIF creation skipped; history not saved.")
