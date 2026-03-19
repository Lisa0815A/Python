#Find duplicate elements.
import numpy as np
arr = np.array([1, 2, 2, 3, 4, 4, 5])
values, counts = np.unique(arr, return_counts=True)
duplicates = values[counts > 1]

print("Duplicate elements:", duplicates)