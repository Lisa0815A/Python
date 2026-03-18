import numpy as np
a = np.arange(9).reshape(1,3,3)
print("matrix :\n",a)
sum = np.sum(a,axis = 2)
print("Column wise sum is :",sum)