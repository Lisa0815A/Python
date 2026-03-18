import numpy as np
a = np.arange(9).reshape(1,3,3)
print("First array :\n",a)
b = np.arange(9).reshape(1,3,3)
print("Second array :\n",b)
sub_arr = a-b
print("substraction of two arrays :\n",sub_arr)