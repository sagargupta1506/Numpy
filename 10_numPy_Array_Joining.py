# Joining the numPy array - here we shall pass concatenate()

import numpy as np
sagar = np.array([1,2,3,4])
sagar1 = np.array([5,6,7,8])

sagar2 = np.concatenate((sagar, sagar1))
print(sagar2)
print('.......................................................')


# Joining the 2-D array along with rows(axis=1)
import numpy as np
sagar = np.array([[1,2],[3,4]])
sagar1 = np.array([[5,6],[7,8]])

sagar2 = np.concatenate((sagar, sagar1), axis=1)
print(sagar2)
print('............................................................')


# Joining the array using the stack function
sagar = np.array([1,2,3,4])
sagar1 = np.array([5,6,7,8])

sagar2 = np.stack((sagar, sagar1), axis=1)
print(sagar2)

print('...............................................................')

# Stacking along with rows : hstack()
sagar = np.array([1,2,3,4])
sagar1 = np.array([5,6,7,8])

sagar2 = np.hstack((sagar, sagar1))
print(sagar2)
print('....................................................................')

# Staccking along with column :
sagar = np.array([1,2,3,4])
sagar1 = np.array([5,6,7,8])

sagar2 = np.vstack((sagar, sagar1))
print(sagar2)
print('..................................................................')


sagar2 = np.dstack((sagar, sagar1))     # - stacking along with height
print(sagar2)