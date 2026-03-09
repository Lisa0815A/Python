import numpy as np
var = np.array([14,23,11,8,75])
print("min :",np.min(var),np.argmin(var))
print("max :",np.max(var),np.argmax(var))
print("sqrt :",np.sqrt(var))

var1 = np.array([[2,1,3],[9,5,6]])
print(np.min(var1,axis = 1))

var2 = np.array([1,2,3])
print(np.sin(var2))
print(np.cumsum(var2))
