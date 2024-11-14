# splitting arrays in numpy - It is reverse to joining, breaking the array
# array_split()

# split the array into 3 parts
import numpy as np
sagar = np.array([1,2,3,4,5,6])
sagar_new = np.array_split(sagar,3)
print(sagar_new)
print('.......................')

# Now we will split the array into 4 parts
import numpy as np
sagar = np.array([1,2,3,4,5,6])
sagar_new = np.array_split(sagar,4)
print(sagar_new)
print('...........................')


# split array by using indexing 

import numpy as np
sagar = np.array([1,2,3,4,5,6])
sagar_new = np.array_split(sagar,3)
print(sagar_new[0])
print(sagar_new[1])
print(sagar_new[2])
print('............................')

# splitting the 2-D array
import numpy as np
sagar = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
sagar_new = np.array_split(sagar,3)
print(sagar_new)
print('.................................')


# split the 2-D array into three 2-D array
import numpy as np
sagar = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
sagar_new = np.array_split(sagar,3)
print(sagar_new)
print('................................')


# splitting the 2-D into three 2-Dalong with rows
import numpy as np
sagar = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
sagar_new = np.array_split(sagar,3, axis=1)     # change only here
print(sagar_new)
print('...................................')


# alternate solution is using the hsplit(), and opposite of  hsplit is hstack()
import numpy as np
sagar = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
sagar_new = np.hsplit(sagar,3)     # change only here
print(sagar_new)





