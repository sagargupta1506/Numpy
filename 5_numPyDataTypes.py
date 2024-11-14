# Data types in python: string, integer, float, boolean, complex

# Data types in numPy:
'''
1- integer for, i
2- boolean for, b
3- unsigned for, u
4- float for, f
5- complex for, c
6- timedelta for, m
7- datatime for, M
8- object for, O
9- string for, S
10- memory for, V
11- unicode string for, U
'''

# Checking the datatype of numPy array - 'dtype'

import numpy as np
sagar = np.array([1,2,3,4])
print(sagar.dtype)

# Checking the datatype of numPy array of string

import numpy as np
sagar = np.array(['apple', "mango", '''grapes'''])
print(sagar.dtype)


# Creating array with a 'defined data type' :

import numpy as np
sagar = np.array([1,2,3,4,5], dtype='i')
sagar = np.array([1,2,3,4,5], dtype='b')
print(sagar)
print(sagar.dtype)

# Now we will create an array with data type of 4 byte int:
import numpy as np
sagar = np.array([1,2,3,4], dtype='i4')
print(sagar)
print(sagar.dtype)


# If a type is given in which the elements cannot be casted then numPy will raise error, what if a value cannot be converted.

import numpy as np
#sagar = np.array(['apple', '2', '3'], dtype='i')        # it generate an error that string cannot be change into integer.
print(sagar)
print(sagar.dtype)


# Converting float datatype in existing array  - astype(),

import numpy as np
sagar = np.array([1.1, 2.1, 3.1, 4.2])
sagar1 = sagar.astype(int)
print(sagar1)
print(sagar1.dtype)

# Converting bool value to integer

import numpy as np
sagar = np.array([1, 0, 3])
sagar1 = sagar.astype(bool)
print(sagar1)
print(sagar1.dtype)

