import numpy as np
a = np.array([10,20,30,40])
norm = ( a - np.min(a) ) / ( np.max(a) - np.min(a))
print("Normalization of array :",norm)