import numpy as np
a = np.arange(6).reshape(2,3)
print("2D array :\n",a)
print("Shape of an array :",a.shape)
b = a.reshape(1,2,3)
print("conversion of 2D into 3D array is :\n",b)
print("shape of an array :\n",b.shape)