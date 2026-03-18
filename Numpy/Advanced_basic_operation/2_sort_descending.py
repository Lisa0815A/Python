#Sort an array in Descending order.
import numpy as np
a = np.array([25,36,12,45,68,94])
print("Array :",a)
print("Descending order of an array :")
b = np.sort(a)[::-1]
print(b)