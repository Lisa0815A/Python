#Split an array into 3 equal parts.
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
result = np.array_split(arr, 3)
print(result)