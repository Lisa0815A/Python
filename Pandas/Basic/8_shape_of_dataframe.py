import pandas as pd
data = {
  "name" : ['a','b','c'],
  "age" : [12,10,14]
}
df = pd.DataFrame(data)
print(df)
print("Shape of Data :",df.shape)