import numpy as np
from mpi4py import MPI

#
# A MapReduce Example
#
#
# Given a set of files, count the frequency of words.


def pprint(str="", end="\n", comm=MPI.COMM_WORLD):
    """Print for MPI parallel programs: Only rank 0 prints *str*."""
    if comm.rank == 0:
        print(str+end, end=' ') 


comm = MPI.COMM_WORLD

pprint("-"*78)
pprint(" Running on %d cores" % comm.size)
pprint("-"*78)


# First Step:
# Split and Distribute (as we don't have a DFS in MPI)




# Second Step: Map
# - Runs for each abstract
# - emit certain words (certain is a global variable)
# emits all words as pairs (word,1)


# Third Step: Reduce
# - Run as Combiner
# - sums up the words values

# Fourth Step: Shuffle
# We will use gather and give it back to the root (not efficient)


### Implementation
# Step 1:
import json


def get_reasonable_records(filename):
    for row in file:
        data = json.loads(row)
        if 'abstract' in data:
            yield data


data = [get_reasonable_records(open('egu24-compact.json'))]

### Real Homework:
###

### Given the matrix (key,value) looking like

'0', 'the abstract one'
'1', 'the abstract two'


### try to find a MPI_Scatter that distributes the work across the cluster.
