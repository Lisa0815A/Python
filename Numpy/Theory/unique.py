import numpy as np
var = np.array([1,2,3,4,5,2,1,2,3,2,4])
x = np.unique(var,return_index=True,return_counts=True)
print(x)