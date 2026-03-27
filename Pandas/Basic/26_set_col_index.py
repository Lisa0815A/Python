import pandas as pd
data = {
  "name": ['lisa','bob','usha','bichi','pabi'],
  "age": [18,12,13,15,16]
}
df = pd.DataFrame(data)
df = df.set_index('name')
print(df)