# Getting some elements out of an existing array and creating a new array is called filtering.
# A boolean index list is a list of boolean corresponding indexes in the array, (true and false)


# Create an array from the elements on index 0 to 2
import numpy as np
sagar = np.array([41,42,43,44])
sagar1 = [True, False, True, False]
finalSagar = sagar[sagar1]
print(finalSagar)
print('.............................')


# Now we shall create a filter array, that will return the greater value of 42
import numpy as np
sagar = np.array([41,42,43,44])
emptySagar = []
for element in sagar:
    if element > 42:
        emptySagar.append(True)
    else:
        emptySagar.append(False)
newSagar = sagar[emptySagar]
print(emptySagar)
print(newSagar)
print('..............................')


# Create a filter array that will return only even elements from the original array.

import numpy as np
sagar = np.array([1,2,3,4,5,6,7,8])
sagarEmpty = []
for i in sagar:
    if i%2 == 0:
        sagarEmpty.append(True)
    else:
        sagarEmpty.append(False)

sagarNew = sagar[sagarEmpty]
print(sagarEmpty)
print(sagarNew)
print('...................................')

# You can also create filter directly from arraya(sort_cut)
import numpy as np
sagar = np.array([41,42,43,44])
sagarempty = sagar > 42
sagarnew = sagar[sagarempty]
print(sagarempty)
print(sagarnew)
