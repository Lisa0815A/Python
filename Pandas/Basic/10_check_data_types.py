import pandas as pd
data = {
  "name" : ['a','b','c'],
  "age" : [12,42,36]
}
df = pd.DataFrame(data)
print(df)
print("Data Type :",df.dtypes)