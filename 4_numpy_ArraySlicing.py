# Slicing Array :- slicing in python means taking element from 1 given index to another index.

# [start:end], [start:end:step]

# Now we shall slice an element from 1 to 5:
import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8,9])
print(sagar[0:5])

print(sagar[3:])        # not providing the last index


# using (-ve) negative slicing

print(sagar[-6:-1])      #from 4 to end, output-[4,5,6,7,8]
print(sagar[-3:])        #from 7 to end, output-[7,8,9]



# Using 'steps': basic maens just ignore the no. of elements

import numpy as np
sag = np.array([1,2,3,4,5,6,7,8,9,10])
print(sag[0:9])
print(sag[0:9:3])       # just ignore 1 value


# now return every other number from the entire array
print(sag[::2])



# Slicing in 2-D array

import numpy as np

sagar = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(sagar[1,1:4])       # output-[7 8 9]

print(sagar[0:2,2])     # output- [3 8]

# print from both index from 1:4
print(sagar[0:2,0:4])        # output-[[1 2 3 4] [6 7 8 9]]