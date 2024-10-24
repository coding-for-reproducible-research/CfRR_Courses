# Run with command:
#
#     $ mpirun -n 2 python mpi_hello_complete.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
if comm.Get_rank() == 0:
    print(f"MPI world size is {comm.Get_size()}")
print(f"Hello from process {comm.Get_rank()}")