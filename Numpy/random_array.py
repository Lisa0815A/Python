""""
rand( ) :The function is used to generate a random value between 0 and 1
randn() :the function is used to generate a random value close to zero this may return positive or negative numbers as well
ranf() :the function for doing random sampling in numpy. it returns an array of specified shape and fills it with random floats in the half open interval [0.0,1.0)
randint():the function is used to generate a random number between given range

"""
#Random Array Generate
#rand()
import numpy as np
vr = np.random.rand(4)
print(vr)
var1 = np.random.rand(2,5)
print(var1)
#randn()
#it gives both positive and negative value
var2=np.random.randn(2,5)
print(var2)
#ranf
#include zero but not include one
var3 = np.random.ranf(4)
print(var3)
#randint()
var4 = np.random.randint(5,20,5)
print(var4)