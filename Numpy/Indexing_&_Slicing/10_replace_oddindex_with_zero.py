import numpy as np
a = np.arange(1,11)
print("array :",a)
a[1::2] = 0
print("after replace :",a)