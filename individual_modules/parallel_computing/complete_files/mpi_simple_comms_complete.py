# Run with command:
#
#     $ mpirun -n 2 python simple_comms_complete.py
from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD

if comm.Get_rank() == 0:
    print("========= 01 Blocking comms =========")
    msg = "Hello!"
    comm.send(msg, dest=1, tag=23)
elif comm.Get_rank() == 1:
    msg = comm.recv(source=0, tag=23)

print(f"{msg} from rank {comm.Get_rank()}")

comm.barrier()

if comm.Get_rank() == 0:
    print("\n========= 02 Non-blocking comms =========")
    msg = "Non-blocking Hello!"
    comm.isend(msg, dest=1, tag=13)
elif comm.Get_rank() == 1:
    req = comm.irecv(source=0, tag=13)
    msg = req.wait()

print(f"{msg} from rank {comm.Get_rank()}")

comm.barrier()

if comm.Get_rank() == 0:
    print("\n========= 03 Array comms =========")
    data = np.arange(0,100,1)
    comm.send(data, dest=1, tag=34)
elif comm.Get_rank() == 1:
    data = comm.recv(source=0, tag=34)
    print(f"Rank {comm.Get_rank()} recieved data:\n{data}")

