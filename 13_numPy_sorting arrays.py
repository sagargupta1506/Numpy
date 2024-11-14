# sort() : in the numPy ndarray object has a function which is called sort(), and this will sort a specified array.

import numpy as np
sagar = np.array([1,9,3,5,6,4])
print(np.sort(sagar))   # this method is lika copy method, here in the original do not have any change.

print('...............................')

sagar1 = np.array(['banana','apple', 'cherry', 'graps', 'pineapple'])
print(np.sort(sagar1))

print('................................')


# sorting into the 2-D array

import numpy as np
sagar = np.array([[3,2,4,1],[9,2,1,6]])
print(np.sort(sagar))

print('.............................')
