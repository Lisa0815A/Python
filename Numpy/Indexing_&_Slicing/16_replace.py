import numpy as np
a = np.array([12,58,69,36,47,67])
print("Array :",a)
a[a>50] = 50
print("in an array all number which is greater than 50 is replacable by 50.")
print("New array :",a)