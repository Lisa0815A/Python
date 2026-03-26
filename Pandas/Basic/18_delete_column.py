import pandas as pd
data = {
  "name": ['a','b','c','d'],
  "age": [12,15,13,15]
}
df = pd.DataFrame(data)
df["city"] = ["BBSR", "Delhi", "Mumbai", "Chennai"]
print(df)
print(df.drop("age",axis=1))