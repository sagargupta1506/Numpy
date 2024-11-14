# Now we will create a numpy ndarray object
# The array object in numpy is called ndarray
# eg: array()

import numpy as np
x = np.array([1,2,3,4,5])   # here we pass the list in array
print(x)

print(type(x))
print('.........................................................')

# We can also pass a list,tuple in any array like object with array method and it will be converted to ndarray

import numpy as np
y = np.array((1,2,3,4,5))   # here pass the tuple in array

print(y)
print(type(y))
print('.............................................................')
# but it change into 'ndarray'

# Dimession in Arrays : a dimenssion arrays is one level of array depth(nested array)

# 0-D Arrays ( Scalars) : are the elements in an array, each value in an array is a 0-D array.

# Now we will create 0-D array with value 42

import numpy as np
z = np.array(42)
print(z)
print('..............................................................')
# Now we will create 1-D array with
# An array that has 0-D arrays as its elements is called uni directional or 1-D
 
import numpy as np
sag = np.array([1,2,3,4])
print(sag)
print('..............................................................')

# Create a 2-D arrat, with certain values

import numpy as np
sagar = np.array([[1,2,3],[4,5,6]])
print(sagar)
print('..............................................................')
# Create a 3-D array with two 2_D array.

import numpy as np
value = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])
print(value)
print('..............................................................')
# check how many dimension in array have : ndim attribute

import numpy as np
a = np.array(89)                                            # 0-D
b = np.array([6,1,8])                                       # 1-D
c = np.array([[4,9,3],[8,0,9]])                             # 2-D
d = np.array([[[7,8,9],[10,11,12]],[[1,2,3],[7,3,0]]])      # 3-D

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print('..............................................................')

# Create and array with 5 dimension and verify that it has 5 dimension

import numpy as np
shar = np.array([1,7,3,5,9], ndmin=5)       # change 1-d to 5-d
print(shar)
print('number of dimensions : ', shar.ndim)