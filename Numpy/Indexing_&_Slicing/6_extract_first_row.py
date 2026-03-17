import numpy as np
a = np.arange(9).reshape(1,3,3)
print("Matrix :\n",a)
b=a[0,0,:]
print("The first row of matrix is :\n",b)
