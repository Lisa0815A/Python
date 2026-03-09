import numpy as np
var = np.array([1,2,3,4])
co = var.copy()
var[1] = 40
print("var :",var)
print("copy :",co) 
print()

var1 = np.array([5,6,7,8])
view = var1.view()
var1[1] = 40
print("var1 :",var1)
print("view :",view)
