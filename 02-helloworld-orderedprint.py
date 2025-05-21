from mpi4py import MPI

comm = MPI.COMM_WORLD

for i in range(comm.size):
    if comm.rank == i:
        print("Hello! I'm rank %d from %d." % (comm.rank, comm.size))
    comm.Barrier()   
# homework for Martin. This does not work with OpenMPI (maybe try MPICH)
