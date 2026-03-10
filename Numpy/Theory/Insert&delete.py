import numpy as np
var = np.array([1,2,3,4])
print(var)
print(var.dtype)
v=np.insert(var,(2,4),40)
print(v)
print()

var1 = np.array([[1,2],[1,2,3]])
v1 = np.insert(var1,2,6,axix=0)
print(v1)