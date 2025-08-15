"""
Aggregate and Visualize Game of Life Benchmark Results

This script loads all benchmarking CSV files matching '../output/gol_timings_*.csv',
processes hardware and method metadata, and generates publication-quality plots:
  1. Performance of each method across different hardware.
  2. Performance of each hardware combination across methods.
  3. Combined overview of all methods and hardware.

Key steps:
- Load and concatenate CSV data into a pandas DataFrame.
- Map raw GPU/CPU strings to concise, human-readable labels.
- Define marker, color, and linestyle mappings for clarity.
- Plot with matplotlib, saving PNGs to '../output'.
"""

# ─────────────────────────────────────────────────────────────────────────────
# Library imports
# ─────────────────────────────────────────────────────────────────────────────

import os, glob, re
import pandas as pd
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────────────────────
# 1) Load all benchmark CSV files into one DataFrame
# ─────────────────────────────────────────────────────────────────────────────
files = glob.glob('../output/gol_timings_*.csv')
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# 2) Define plotting markers for each method
# ─────────────────────────────────────────────────────────────────────────────
marker_map = {
    'naive': 's',
    'numpy': 'o',
    'cupy': '^',
}

# ─────────────────────────────────────────────────────────────────────────────
# 3) Shorten and clean hardware labels for legibility
# ─────────────────────────────────────────────────────────────────────────────
def short_gpu(name):
    """
    Map raw GPU names to concise labels for plot legends.

    Args:
        name: Original GPU string from CSV.

    Returns:
        A shorter, human-readable GPU label.
    """
    if 'A100'   in name: return 'NV A100'
    if '3070'   in name: return 'NV RTX 3070'
    if 'H100'   in name: return 'NV H100'
    return name

def short_cpu(name):
    """
    Simplify raw CPU strings using regex to extract brand and core count.

    Args:
        name: Original CPU string from CSV.

    Returns:
        A shorter, human-readable CPU label.
    """
    m = re.search(r'(AMD).*?_(\d+)-Core', name, flags=re.IGNORECASE)
    if m:
        brand, cores = m.group(1).upper(), m.group(2)
        return f"{brand} {cores} Core"
    return name.replace('_', ' ')

def base_method(method_str):
    """
    Strip any parenthetical notes from method names (e.g. "NumPy (CPU)" → "NumPy").

    Args:
        method_str: Full method label from CSV.

    Returns:
        Clean method name without parentheses.
    """
    return re.sub(r'\s*\(.*\)', '', method_str).strip()

# ─────────────────────────────────────────────────────────────────────────────
# 4) Build style map for each unique (GPU, CPU) combination
# ─────────────────────────────────────────────────────────────────────────────
combos = df[['gpu','cpu']].drop_duplicates().values.tolist()

# Color-blind safe palette (Paul Tol six):
colors = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377']
# Linestyles for up to 6 combos:
linestyles = ['-', '--', '-.', ':', (0, (1,1)), (0, (5,1))]

style_map = {}
for idx, (gpu, cpu) in enumerate(combos):
    style_map[(gpu, cpu)] = {
        'color':     colors[idx % len(colors)],
        'linestyle': linestyles[idx % len(linestyles)]
    }

legend_kwargs = dict(fontsize='small')

# ─────────────────────────────────────────────────────────────────────────────
# 5) Plotting helper function
# ─────────────────────────────────────────────────────────────────────────────
def make_plot(grouped, title, fname, legend_args):
    """
    Generate and save a line plot with error bars for grouped benchmark data.

    Args:
        grouped: pandas GroupBy object grouping DataFrame by (gpu, cpu, method).
        title:   Title string for the plot.
        fname:   Filename (PNG) to save under '../output/'.
        legend_args: Extra arguments for ax.legend().
    """
    fig, ax = plt.subplots(figsize=(8,6))

    for (gpu, cpu, method), g in grouped:
        bm      = base_method(method)
        bm_low  = bm.lower()
        marker  = marker_map[bm_low]
        style   = style_map[(gpu, cpu)]
        label   = f"{bm}\nCPU: {short_cpu(cpu)}\nGPU: {short_gpu(gpu)}"

        ax.plot(
            g['grid_size'],
            g['mean_time_sec'],
            marker=marker,
            color=style['color'],
            linestyle=style['linestyle'],
            label=label
        )

    ax.set(
        xlabel='Grid Size',
        ylabel='Mean Time (s)',
        title=title
    )
    ax.legend(**legend_kwargs, **legend_args)
    fig.tight_layout(rect=[0,0,1,1])
    fig.savefig(f"../output/{fname}", bbox_inches='tight', dpi=300)
    plt.close(fig)

# ─────────────────────────────────────────────────────────────────────────────
# 6) Generate plots: method-specific across hardware
# ─────────────────────────────────────────────────────────────────────────────
for method in df['method'].unique():
    sub = df[df['method']==method].sort_values('grid_size')
    grp = sub.groupby(['gpu','cpu','method'])
    make_plot(
        grp,
        title=f"{base_method(method)} Across Hardware",
        fname=f"{base_method(method).lower()}_across_hardware.png",
        legend_args={'loc':'best', 'ncol':1}
    )

# ─────────────────────────────────────────────────────────────────────────────
# 7) Hardware-specific across methods
# ─────────────────────────────────────────────────────────────────────────────
for (gpu,cpu), sub in df.groupby(['gpu','cpu']):
    grp = sub.sort_values('grid_size').groupby(['gpu','cpu','method'])
    cpu_s = cpu.lower().replace(' ','_').replace('/','_')
    gpu_s = short_gpu(gpu).replace(' ','_').lower()
    make_plot(
        grp,
        title=f"{short_cpu(cpu)} + {short_gpu(gpu)}",
        fname=f"perf_{cpu_s}_{gpu_s}.png",
        legend_args={'loc':'best', 'ncol':1}
    )

# ─────────────────────────────────────────────────────────────────────────────
# 8) Combined plot of all methods & hardware
# ─────────────────────────────────────────────────────────────────────────────
grp_all = df.sort_values(['gpu','cpu','method','grid_size'])\
            .groupby(['gpu','cpu','method'])
make_plot(
    grp_all,
    title="All Methods & Hardware",
    fname="all_methods_hardware.png",
    legend_args={
        'loc':'center left',
        'bbox_to_anchor':(1,0.5),
        'ncol':1
    }
)

print("All plots saved to ../output") 
