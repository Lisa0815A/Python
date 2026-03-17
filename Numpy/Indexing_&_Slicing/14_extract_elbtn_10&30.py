import numpy as np
a = np.array([32,14,8,5,86])
print("array :",a)
b = a[(a>10) & (a<30)]
print("element between 10 and 30 :",b) 
