#Count frequency of element
import numpy as np
arr = np.array([1,2,2,3,3,3,4])
values,counts = np.unique(arr,return_counts=True)
print("Vlues :",values)
print("Frequency :",counts)