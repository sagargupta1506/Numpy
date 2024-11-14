# Searching Array : you can search for a certain value and return the indexes that get the match. by using where()

import numpy as np
sagar = np.array([1,2,3,4,5,4,4])
sagar_new = np.where(sagar == 4)        # it gives the indexing of the given value in array.
print(sagar_new)
print('......................')


# Now we shall find the  indexes where the values are even:
sagar = np.array([1,2,3,4,5,6,7,8,9])
sagar1 = np.where(sagar%2==0)           # the outpue[1,3,5,7], are the 'index number' not the number.
print(sagar1)

print('..............................')

# Now we shall find the indexes where the values are odd:
sagar = np.array([1,2,3,4,5,6,7,8,9])
sagar2 = np.where(sagar%2==1)  # the output[2,4,6,8], are the 'index number', not the number.
print(sagar2) 

print('.................................')

# searchsorted()  - 'perform binary search in array', always keep in mind that in the numPy array the output will almost is index number not the number

# We shall now find the index, where the value 7 should be inserted.

import numpy as np
sagar = np.array([4,5,6,7,8,9])
sagar1 = np.searchsorted(sagar,7)
print(sagar1)
print('..............................')

# Searching for the multiple values
import numpy as np
sarad = np.array([1,3,5,7])
sarad1 = np.searchsorted(sarad, [2,4,6]) 
print(sarad1)


