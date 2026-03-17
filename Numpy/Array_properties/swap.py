import numpy as np
#1D to 2D Array
a = np.array([[1,2,3],
              [4,5,6]])
print("Original shape:",a.shape)
b = np.swapaxes(a,0,1)
print("new shape :",b.shape)
print(b)

#2D-3D Array
c = np.arange(24).reshape(2,3,4)
print("original array :\n",c)
print("original shape :\n",c.shape)
d = np.swapaxes(c,0,2)
print("view array :\n",d)
print("shape of an array:\n",d.shape) 