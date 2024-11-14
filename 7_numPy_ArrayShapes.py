# The shape of an array is the number of elements in each dimension.
# Now we shall try to get the shape of any array

import numpy as np
sagar = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(sagar.shape)

# (2, 5), it means that the array has 2-dimension, and each dimension contain 5 elements.

# Now we will create a 5-D array by using 'ndmin'.

import numpy as np
sagar = np.array([1,2,3,4], ndmin=5)
print(sagar)

print('Shape of array is : ', sagar.shape)  # here the 'nested' array concept is used, output is (1,1,1,1,4), all the 1 means that each has inside 1 array and in the 5 th array has 4 elements.
