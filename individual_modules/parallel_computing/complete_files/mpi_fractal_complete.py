# Run with command:
# $ mpirun -n X python parallel_fractal_complete.py
from mpi4py import MPI
import numpy as np
import warnings
import matplotlib.pyplot as plt


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
cells = 4000

comm = MPI.COMM_WORLD

if comm.Get_rank() == 0:
    grid = complex_grid(extent, cells)
    grid = np.array_split(grid, comm.Get_size())
else:
    grid = None

grid = comm.scatter(grid, root=0)

fractal = julia_set(grid, 80, c)

fractal = comm.gather(fractal, root=0)
if not fractal is None:
    fractal = np.concatenate(fractal)

#if comm.Get_rank() == 0:
#    plt.imshow(fractal, extent=[-extent, extent, -extent, extent], aspect='equal')
#    plt.show()