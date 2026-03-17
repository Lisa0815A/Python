import numpy as np
a = np.arange(24).reshape(1,6,4)
print("matrix :\n",a)
print("shape of a above matrix :",a.shape)
b = a[0,0:3,0:3]
print("3x3 matrix :\n",b)
 