import pandas as pd
data = {
  "name":['lisa',None,'usha','bichi','pabi'],
  "age":[None,12,13,15,16,]
}
df = pd.DataFrame(data)
print(df)
print("Any missing value exist :",df.isnull().values.any())
print(df.dropna())
print(df.dropna(axis = 1))
print(df.dropna(how ='all'))
print(df.dropna(how ='any'))

#df['age'] = df['age'].fillna(df['age'].mean())
df['age'].fillna(18, inplace=True)