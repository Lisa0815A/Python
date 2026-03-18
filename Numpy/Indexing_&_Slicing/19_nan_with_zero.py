import numpy as np
a = np.array([12,np.nan,36,np.nan])
new_a = np.nan_to_num(a,nan=5)
print("Array :",a)
print("new_Array :",new_a)