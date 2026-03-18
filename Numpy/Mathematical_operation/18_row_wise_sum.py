import numpy as np
a = np.arange(9).reshape(1,3,3)
print("Array :\n",a)
sum = np.sum(a,axis =1)
print("Row wise sum :",sum)