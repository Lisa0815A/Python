import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

common = np.intersect1d(a, b)

print("Common elements:", common)