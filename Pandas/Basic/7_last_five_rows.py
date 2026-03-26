import pandas as pd
data = {
  "name" : ['a','b','c','d','e','f','g'],
  "age" : [12,32,24,25,26,84,56,]  
}
df = pd.DataFrame(data)
print(df)
print("Last five rows are :")
print(df.tail())