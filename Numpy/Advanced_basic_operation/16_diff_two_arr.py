#Find difference between two arrays.
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

diff = np.setdiff1d(a, b)

print("Elements in A not in B:", diff)