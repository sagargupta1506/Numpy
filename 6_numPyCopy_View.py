# difference between numPy array copy vs view

# first we will make a copy, and change into original array, and display both

import numpy as np
sagar = np.array([1,2,3,4,5])

sagar1 = sagar.copy()
sagar1[0] = 93
print(sagar)
print(sagar1)

# Now will change and display both

import numpy as np
sagar = np.array([1,2,3,4,5])
sagar1 = sagar.view()
sagar[0] = 42

print(sagar)
print(sagar1)