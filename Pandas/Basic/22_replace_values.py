#replace values in dataframe
import pandas as pd
data = {
  "name":['lisa','bob','usha','bichi','pabi'],
  "age":[18,12,13,15,16,]
}
df = pd.DataFrame(data)
print(df)
df['age'] = df['age'].replace(12,100)
print(df)