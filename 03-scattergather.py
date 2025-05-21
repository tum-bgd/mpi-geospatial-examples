import numpy as np
from mpi4py import MPI

def rprint(msg,*args,comm=MPI.COMM_WORLD,rank=0, **kwargs):
    "Rank Print prints on a specific rank only"
    if rank is None or comm.rank == rank:
        print(msg,*args,*kwargs)

comm = MPI.COMM_WORLD

rprint("Setup: %d processes" %(comm.size))
rprint("Phase 1: Input Data Preparation")
my_N = 4
N = my_N * comm.size

if comm.rank == 0:
    A = np.arange(N, dtype=np.float64)
else:
    A = np.empty(N, dtype=np.float64)

my_A = np.empty(my_N, dtype=np.float64)

###
rprint("I am %d and my A is: %s" %(comm.rank, str(A)))
comm.Barrier();
rprint("Phase 2: Scattering Data Across Cluster" )

comm.Scatter( [A, MPI.DOUBLE], [my_A, MPI.DOUBLE] )

rprint(">> Data after Scatter")
for r in range(comm.size):
    if comm.rank == r:
        print("[%d] %s" % (comm.rank, my_A))
    comm.Barrier()

## Parallel Work Section
my_A *= 2;
## End Parallel Work Section
comm.Barrier();

rprint("Phase 3: Gather")

### now, we gather it back to the coordinator rank 0
## https://mpi4py.readthedocs.io/en/4.0.3/reference/mpi4py.MPI.Comm.html#mpi4py.MPI.

## Option One: gather to 0
#comm.Gather(my_A, A,0) # gather myA into A on node 0
## Option Two: Gather anywhere
comm.Allgather(my_A, A) # gather myA into A on node 0

comm.Barrier()
rprint("Final Result")
print("I am %d and my A is: %s" %(comm.rank, str(A)))

