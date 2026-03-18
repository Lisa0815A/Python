import numpy as np
a = np.arange(9).reshape(1,3,3)
print("First array :\n",a)
b = np.arange(9).reshape(1,3,3)
print("Second array :\n",b)
sum_arr = a+b
print("Addition of two arrays :\n",sum_arr)