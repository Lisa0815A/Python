import numpy as np
arr = np.array([1,2,3,4])
arr_copy = arr.copy()
arr_copy[0] = 100
print("original array :",arr)
print("copy array :",arr_copy)