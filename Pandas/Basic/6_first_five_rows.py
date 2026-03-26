import pandas as pd
data = {
  "name" : ['lisa','lija','usha','pabi','bichi'],
  "age" : [21,23,24,30,34]
}
df = pd.DataFrame(data)
print(df)
print(df.head())