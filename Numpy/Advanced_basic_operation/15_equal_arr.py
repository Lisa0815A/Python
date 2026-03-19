# Check two arrays are equal or not
import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

result = np.array_equal(a, b)

print("Arrays are equal:", result)