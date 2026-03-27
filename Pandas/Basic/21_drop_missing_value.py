#Drop missing values
import pandas as pd
data = {
  "name":['lisa',None,'usha','bichi','pabi'],
  "age":[None,12,13,15,16,]
}
df = pd.DataFrame(data)
data_clean = df.dropna()
print(data_clean)