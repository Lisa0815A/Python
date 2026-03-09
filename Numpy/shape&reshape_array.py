#shape
import numpy as np
var = np.array([[1,2,3,4],[1,2,3,4]])
print(var)
print()
print(var.shape)
print()
var1 = np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)
#Reshape
var2 = np.array([1,2,3,4,5,6])
print(var2)
print(var2.ndim)
print()
x = var2.reshape(3,2) 
print(x)
print(x.ndim)