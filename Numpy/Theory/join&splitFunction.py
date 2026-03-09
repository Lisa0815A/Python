"""
join Array - Joining means putting contents of two or more arrays in a single array.
"""
import numpy as np
var1 = np.array([1,2,3,4])
var2 = np.array([9,8,7,6])
ar = np.concatenate((var1,var2))
print(ar)