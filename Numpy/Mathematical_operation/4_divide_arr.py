import numpy as np
a = np.arange(9).reshape(1,3,3)
print("First array :\n",a)
b = np.arange(9).reshape(1,3,3)
print("Second array :\n",b)
div_arr = a/b
print("division of two arrays :\n",div_arr)