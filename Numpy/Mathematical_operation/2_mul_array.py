import numpy as np
a = np.arange(9).reshape(1,3,3)
print("First array :\n",a)
b = np.arange(9).reshape(1,3,3)
print("Second array :\n",b)
mul_arr = a*b
print("multiplication of two arrays :\n",mul_arr)