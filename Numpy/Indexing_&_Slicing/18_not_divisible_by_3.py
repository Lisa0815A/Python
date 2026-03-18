import numpy as np
a = np.array([15,89,36,12,45])
print("Array :",a)
b = a[a%3 != 0]
print("All element selected which is not divisible by 3 :\n",b)
