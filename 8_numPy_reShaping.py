# reShaping : it means that the changine the shape of an array, like adding or removing the elements.

# reShaping from 1-D to 2-D
import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

sagar1 = sagar.reshape(4, 3)    # divide the whole array into 4 parts and each part has 3 elements.

print(sagar1)
print('...................')


# reShaping from 1-D to 3-D
import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])  

sagar2 = sagar.reshape(2, 3, 2)  # first '2' means, the whole array divide into 2 part, and every part has again '3' part and last '2' means, each 3 part has 2 element.

print(sagar2)
print('...........................')


# Revise the last chapter copy and view

import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8])
print(sagar.reshape(2,4).base)          # This is view.
print('...................................')

# Unknown dimension - you are only allowed to have one unknown dimension. and we pass '-1'

import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8])

sagar3 = sagar.reshape(2,2,-1)   # here '-1' represent 2, and it automatically detect that, if your array has elements to divide into 3 elements, then '-1' represent 3.

print(sagar3)
print('.............................')

if_


# Flattening the array, by converting multidimensional array in 1-D array.
# Change 2-D array into 1-D array(both statements are same).

import numpy as np
sagar = np.array([[1,2,3],[4,5,6]])
sagar1 = sagar.reshape(-1)
print(sagar1) 



# There are alot of functions for changing the shapes of an array in numPy, like flatten, ravel, and we can also rearrnging the element, rot90, fliplr, flipud, these all the belongs to the advanced numPy.


