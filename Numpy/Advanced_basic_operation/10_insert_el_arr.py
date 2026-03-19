#Insert an element into an array.
import numpy as np
arr = np.array([1, 2, 3, 4])
new_arr = np.insert(arr, 2, 99)

print("After insertion:", new_arr)