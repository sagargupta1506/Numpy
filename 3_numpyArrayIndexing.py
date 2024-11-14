# Array indexing is the same accessing an array element:
# and array indexing start with 0
# 1-D array
import numpy as np
sagar = np.array([1,2,3,4])
print(sagar[2])
print('................................')

# we can get the third and forth elements from adding them

import numpy as np
sharad = np.array([1,2,5,4])
print(sharad[2] + sharad[3])
print('................................')

# Accessing the 2-D its like rows and columns.

import numpy as np
sharad = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('1st element in the 0th row : ', sharad[0, 1])
print('4th element in the 1st row : ', sharad[1, 4])
print('................................')

# Accessing the 3-D, same as accessing

import numpy as np

sagar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(sagar[0, 1, 2])       # 6
print(sagar[1, 0, 0])       # 7
