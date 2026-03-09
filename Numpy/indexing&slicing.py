import numpy as np
var = np.array([9,8,7,6,5])
#               0,1,2,3,4
#              -5,-4,-3,-2,-1 
print(var[2])
print(var[-3])

var1 = np.array([[9,8,7],[4,5,6]]) 
print(var1)
print()
var2 = np.array([[1,2],[6,7]])
print(var2[0,1])
print(var2.ndim)