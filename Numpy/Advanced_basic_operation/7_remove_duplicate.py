#Remove duplicates from an array.
import numpy as np
arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_arr = np.unique(arr)
print("Array after removing duplicates:", unique_arr)