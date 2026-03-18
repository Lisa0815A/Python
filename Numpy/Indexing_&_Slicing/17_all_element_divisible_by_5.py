import numpy as np
a = np.array([10,3,45,69,75]) 
b = a[a%5 == 0]
print("all divisible by 5 :",b)