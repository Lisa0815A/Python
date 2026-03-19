#Count elements greater than 10.
import numpy as np
arr = np.array([8,12,3,86,45,7])
values = arr[arr>10]
count =len(values)
print("Numbers greater than 10 is :",values)
print("Count :",count)