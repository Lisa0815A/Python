import pandas as pd
data  = {
  "name" : ['a','b','c','d'],
  "age" : [12,15,13,15]
}
df = pd.DataFrame(data)
print(df)
print("Columns name :",df.columns)