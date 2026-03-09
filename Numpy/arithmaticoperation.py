"""
Arithmatic operation in numpy arrays

a+b  np.add(a,b)
a-b  np.substract(a,b)
a*b  np.multiply(a,b)
a/b  np.divide(a,b)
a%b  np.mod(a,b)
a**b np.power(a,b)
1/a  np.reciprocal(a)

"""
import numpy as np
var = np.array([1,2,3,4])
varadd = var+3
print(varadd)
print()
var1 = np.array([1,2,3,4])
var2 = np.array([1,2,3,4])
varadd = var1 + var2
print(varadd)
#2D Array
var21 = np.array([[1,2,3,4],[1,2,3,4]])
var22 = np.array([[1,2,3,4],[1,2,3,4]])
print(var21)
print()
print(var22)
print()
varadd2 = var21 + var22
print(varadd2)