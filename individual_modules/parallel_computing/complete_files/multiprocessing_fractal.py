# Run with command:
# $ python multiprocessing_fractal.py
import numpy as np
import warnings
import matplotlib.pyplot as plt
from functools import partial
from multiprocessing import Pool

def complex_grid(extent, n_cells):
    mesh_range = np.arange(-extent, extent, extent/n_cells)
    x, y = np.meshgrid(mesh_range * 1j, mesh_range)
    z = x + y

    return z


def julia_set(grid, num_iter, c):

    fractal = np.zeros(np.shape(grid))

    # Iterate through the operation z := z**2 + c.
    for j in range(num_iter):
        # Catch the warnings because they are annoying
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            grid = grid ** 2 + c
            index = np.abs(grid) < np.inf
        fractal[index] = fractal[index] + 1

    return fractal

c = -0.83 - 0.22 * 1j
extent = 2
cells = 2000

grid = complex_grid(extent, cells)

# Parameters for multiprocessing
n_processes = 5
n_slices = 2000

# Split up the grid to distribute to processes
sliced_grid = np.array_split(grid, n_slices)
with Pool(processes=n_processes) as p:
    fractals = p.map(partial(julia_set, num_iter=80, c=c) , sliced_grid)

fractal = np.concatenate(fractals)

#plt.imshow(fractal, extent=[-extent, extent, -extent, extent], aspect='equal')
#plt.show()
