# Game of Life simulation with detailed comments explaining each part of the code.

import argparse      # For parsing command-line arguments
import time          # For measuring wall-clock time
import resource      # For measuring CPU and memory usage
from pathlib import Path  # For convenient file path handling

import numpy as np                           # Numerical operations on arrays
import matplotlib.pyplot as plt              # Plotting figures and images
import matplotlib.animation as animation     # Creating animated GIFs
from tqdm import tqdm                        # Progress bar for loops


def life_step_int(grid: np.ndarray, neighbours: np.ndarray) -> np.ndarray:
    """
    Perform a single step (generation) update for Conway's Game of Life.

    Parameters:
    - grid (np.ndarray): 2D uint8 array of shape (N, N) with values 0 (dead) or 1 (alive).
    - neighbours (np.ndarray): 2D uint8 array of same shape used for counting neighbours.

    Returns:
    - np.ndarray: New 2D uint8 array representing next generation.
    """
    # Reset neighbour counts to zero for current iteration
    neighbours.fill(0)

    # Iterate through the eight possible neighbour offsets
    for dx, dy in (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ):
        # Roll the grid in x (rows) and y (columns), then accumulate counts
        neighbours += np.roll(np.roll(grid, dx, axis=0), dy, axis=1)

    # Apply rules:
    # - A dead cell with exactly 3 neighbours becomes alive (birth).
    # - A live cell with 2 or 3 neighbours stays alive (survival).
    # Convert boolean mask back to uint8.
    return ((neighbours == 3) | ((grid == 1) & (neighbours == 2))).astype(np.uint8)


def simulate_and_animate(
    N: int,
    timesteps: int,
    p_alive: float,
    output_file: Path,
    interval_ms: int = 200,
    max_display: int = 1080,
    dpi: int = 180
) -> np.ndarray:
    """
    Initialize the Game of Life grid randomly, run simulation, create a GIF,
    and count alive occurrences per cell over time.

    Parameters:
    - N: Grid width/height
    - timesteps: Number of generations
    - p_alive: Initial probability of a cell being alive
    - output_file: Path to save the GIF
    - interval_ms: Frame interval in milliseconds
    - max_display: Maximum pixel dimension for display (downsample if larger)
    - dpi: Output resolution

    Returns:
    - counts: 2D uint32 array of shape (N, N) with number of times each cell was alive
    """
    rng = np.random.default_rng()  # Random number generator

    # Create initial grid: randomly set cells alive based on threshold
    grid = np.empty((N, N), dtype=np.uint8)
    threshold = int(p_alive * 1_000_000)
    for i in range(N):
        # Generate random integers and compare to threshold for alive/dead
        random_row = rng.integers(0, 1_000_000, size=N, dtype=np.int32)
        grid[i, :] = (random_row < threshold).astype(np.uint8)

    neighbours = np.zeros((N, N), dtype=np.uint8)  # Buffer for neighbour counts
    counts = np.zeros((N, N), dtype=np.uint32)    # Alive counts accumulator

    # Determine downsampling step to fit within max_display
    step = 1 if max_display is None or max_display >= N else max(1, N // max_display)

    # Set up Matplotlib figure without axes for clean frames
    width_in = max_display / dpi
    fig = plt.figure(figsize=(width_in, width_in), frameon=False)
    fig.patch.set_visible(False)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_axis_off()

    # Display initial frame (possibly downsampled)
    small = grid[::step, ::step]
    im = ax.imshow(
        small,
        cmap='binary',  # black-white colormap
        vmin=0, vmax=1,
        interpolation='nearest'
    )

    # Configure GIF writer: frames per second = 1000 / interval_ms
    writer = animation.PillowWriter(fps=1000 / interval_ms)
    writer.setup(fig, str(output_file), dpi=dpi)

    # Main simulation loop with progress bar
    for _ in tqdm(range(timesteps), desc="Simulating & writing GIF"):
        counts += grid            # Update alive counts
        small = grid[::step, ::step]
        im.set_data(small)        # Update image data for frame
        writer.grab_frame()       # Write frame to GIF
        grid = life_step_int(grid, neighbours)  # Compute next generation

    writer.finish()  # Finalize GIF file
    plt.close(fig)   # Close figure to free memory

    return counts


def plot_heatmap(counts: np.ndarray, output_file: Path = None):
    """
    Generate a heatmap of cell alive counts and save or display it.

    Parameters:
    - counts: 2D array of alive counts per cell
    - output_file: Optional Path to save the heatmap image (PNG). Show interactively if None.
    """
    plt.figure(figsize=(4, 4))
    plt.imshow(counts, cmap='hot', interpolation='nearest')  # Use 'hot' colormap
    plt.colorbar(label='Alive Count')  # Show scale of counts
    plt.title('Cell Alive Counts Heatmap')
    plt.axis('off')  # Hide axes for clarity

    if output_file:
        plt.savefig(output_file, dpi=150, bbox_inches='tight', pad_inches=0)
        print(f"Heatmap saved to {output_file}")  # Log save location
    else:
        plt.show()  # Display on screen if no output path provided


def main():
    """
    Entry point for command-line execution. Parses arguments, runs simulation,
    generates GIF and heatmap, and reports resource usage.
    """
    # Set up argument parser with descriptions and defaults
    parser = argparse.ArgumentParser(description="Game of Life with Heatmap (all-int, streaming HD GIF)")
    parser.add_argument("--size", type=int, default=100, help="Grid dimension (N×N)")
    parser.add_argument("--timesteps", type=int, default=50, help="Number of generations to simulate")
    parser.add_argument("--p-alive", type=float, default=0.2, help="Initial alive probability (0–1)")
    parser.add_argument("--output", type=Path, default=Path("game_of_life_hd.gif"), help="Output GIF filename")
    parser.add_argument("--heatmap", type=Path, default=Path("alive_heatmap.png"), help="Output heatmap filename (PNG)")
    parser.add_argument("--interval", type=int, default=200, help="Frame duration in ms")
    parser.add_argument("--max-display", type=int, default=1080, help="Max side length for display (pixels)")
    parser.add_argument("--dpi", type=int, default=180, help="Resolution (dots per inch) for outputs")
    args = parser.parse_args()

    # Log parameters for user reference
    print(f"[All-int Matplotlib HD + Heatmap] size={args.size}, timesteps={args.timesteps}, p_alive={args.p_alive}")

    # Record start times for benchmarking
    start_wall = time.perf_counter()
    rstart = resource.getrusage(resource.RUSAGE_SELF)

    # Run simulation and animation
    counts = simulate_and_animate(
        N=args.size,
        timesteps=args.timesteps,
        p_alive=args.p_alive,
        output_file=args.output,
        interval_ms=args.interval,
        max_display=args.max_display,
        dpi=args.dpi
    )

    # Plot and save the heatmap of alive counts
    plot_heatmap(counts, args.heatmap)

    # Record end times for benchmarking
    end_wall = time.perf_counter()
    rend = resource.getrusage(resource.RUSAGE_SELF)

    # Compute and display resource usage
    elapsed = end_wall - start_wall
    cpu_user = rend.ru_utime - rstart.ru_utime
    cpu_system = rend.ru_stime - rstart.ru_stime
    peak_rss = rend.ru_maxrss / (1024 ** 2)  # Convert KB to GB

    print(f"Saved HD GIF to {args.output}")
    print(f"Saved heatmap to {args.heatmap}\n")
    print("=== Resource usage ===")
    print(f"Wall-clock time : {elapsed:.2f} s")
    print(f"CPU time         : user {cpu_user:.2f} s, system {cpu_system:.2f} s")
    print(f"Peak memory (RSS): {peak_rss:.2f} GB")


if __name__ == "__main__":
    main()
