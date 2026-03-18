import numpy as np
a = np.array([12,58,64,32,26,98,77])
print("array :",a)
b = a[a>50]
print("Indices of element greaterthan 50 is:",b.index())