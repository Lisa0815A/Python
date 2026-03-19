#Create a Series from a list
import pandas as pd
data = [10,20,30,40,50,60]
print("List :",data)
s = pd.Series(data)
s1 = pd.Series(data,index=['a','b','c','d','e','f'],name = "My series")
print("Series :\n",s)
print("Changable series index :\n",s1)