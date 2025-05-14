## Analysis
# Come up with an expression that describes the resource consumption of the algorithm.
# We will do this by attempting to describe it in terms of what the code is doing in a conside
# and accurate manner.

### Example 1
# Perform an analysis of this function with respect to size of the array
def add(array):
    rc = 0
    for i in range(len(array)):
        rc+= array[i]
    return rc

#### Solution
def add(array):
    rc = 0
    for i in range(len(array)):
        rc+= array[i]
    return rc