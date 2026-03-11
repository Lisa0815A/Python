import numpy as np
#create array divisible by 3 from 1 to 50
arr = np.arange(3,51,3)
print("method 1 :")
print(arr)

#method 2
ar = np.arange(1,51)
result = ar[ ar%3 == 0 ]
print("method 2 :")
print(result)