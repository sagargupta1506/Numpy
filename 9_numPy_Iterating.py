# Iteraing Array : means going through the elements one by one, just like looping

# Iterate the element of 1-D
import numpy as np
sagar = np.array([1,2,3,4,5])
for i in sagar:
    print(i)
print('.......................')



# Iterate in 2-D
import numpy as np
sagar = np.array([[1,2,3],[4,5,6]])
for i in sagar:
    print(i)

print('.........................')



# Iterate on each element(scalar), in 2-D,
import numpy as np
sagar = np.array([[8,2,9],[1,3,9]])
for i in sagar:
    for a in i:
        print(a)
print('..........................')



# Iterate in 3-D
import numpy as np
sagar = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])

for i in sagar:
    for a in i:
        for b in a:
            print(b)
print('...............................')

# Iterating arrays, using the nditer(), this is helping function

# Now we shall iterate on each scalar element

import numpy as np
sagar = np.array([[[1,2],[3,4],[5,6,],[7,8]]])
for i in np.nditer(sagar):
    print(i)

print('...............................')

# Now we shall iterate with different step sizes.

import numpy as np
sagar = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(sagar[:,::2]):
    print(i)
