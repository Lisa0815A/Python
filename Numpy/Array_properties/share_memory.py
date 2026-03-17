import numpy as np
a = np.array([1,2,3,4])
b=a[1:3]  #slicing->view (shares memory) 
print(a)
print(b)
print(np.shares_memory(a,b))