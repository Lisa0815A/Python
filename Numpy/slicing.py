import numpy as np
var = np.array([1,2,3,4,5,6,7])
#               0,1,2,3,4,5,6
print(var)
print()
print("2 to 5 :",var[1:5])
print("2 to end :",var[1:])
print("start to 5 :",var[:5])
print("stop :",var[1:6:2])

var1 = np.array([[1,2,3,4,5],[9,8,7,6,5],[11,12,13,14,15]])
print(var1)
print("8 to 5 :",var1[1,1:])