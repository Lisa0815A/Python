import pandas as pd
data = {
  "name" : ['jack','bob','robert',None],
  "age" : [12,43,None,16]
}
df = pd.DataFrame(data)
print(df)
print("Missing value :\n",df.isna())
print("Each column missing value :\n",df.isnull().sum())
print("Total missing value :\n",df.isnull().sum().sum())