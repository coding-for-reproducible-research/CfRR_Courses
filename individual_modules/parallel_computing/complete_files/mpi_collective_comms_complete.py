# Run with command:
#
#     $ mpirun -n 4 python collective_comms_complete.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

if comm.Get_rank() == 0:
    print("========== 01 Simple broadcast ==========")
    msg = "Broadcasted message hello"
else:
    msg = None

msg = comm.bcast(msg, root=0)

print(f"{msg} from rank {comm.Get_rank()}")
comm.barrier()

if comm.Get_rank() == 0:
    print("\n========== 02 Simple scatter/gather ==========")
    rng = np.random.default_rng()
    data = rng.integers(low=0, high=10, size=comm.Get_size())
    print(f"Rank 0 data is {data}")
else:
    data = None

data = comm.scatter(data, root=0)

print(f"Rank {comm.Get_rank()} recieved data entry: {data}")
comm.barrier()

data = comm.gather(data, root=0)

print(f"Post gather: Rank {comm.Get_rank()} has data: {data}")
comm.barrier()

if comm.Get_rank() == 0:
    print("\n========== 03 Array scatter ==========")
    data = np.arange(200)
    print(f"Rank 0 data is {data}")
    data = np.array_split(data, comm.Get_size())
else:
    data = None

data = comm.scatter(data, root=0)

print(f"Rank {comm.Get_rank()} recieved data entry: {data}")
comm.barrier()

data = comm.gather(data, root=0)
if not data is None:
    data = np.concatenate(data)

print(f"Post gather: Rank {comm.Get_rank()} has data: {data}")
comm.barrier()


if comm.Get_rank() == 0:
    print("\n========== 04 Global operations ==========")
    data = np.arange(1, 101, 5)
    print(data)
    print(f"Sum of rank 0 data is {np.sum(data)}")
    print(f"Product of rank 0 data is {np.prod(data)}")
    data = np.array_split(data, comm.Get_size())
else:
    data = None

data = comm.scatter(data, root=0)

glob_sum = comm.reduce(data, MPI.SUM, root=0)
glob_prod = comm.reduce(data, MPI.PROD, root=0)

if comm.Get_rank() == 0:
    print(f"MPI global sum of data is {np.sum(glob_sum)}")
    print(f"MPI global product of data is {np.prod(glob_prod)}")