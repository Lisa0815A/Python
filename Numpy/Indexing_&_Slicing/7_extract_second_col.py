import numpy as np
a = np.arange(6).reshape(1,2,3)
print("matrix :\n",a)
print("matrix shape :",a.shape)
b=a[0,:,1]
print("extract column 2 is :",b)
