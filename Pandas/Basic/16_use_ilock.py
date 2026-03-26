import pandas as pd
data = {
  "name" : ['a','b','c','d'],
  "age" : [12,14,36,42],
  "city" : ["Agra","kuchh","Mumbai","Delhi"] 
}
df = pd.DataFrame(data)
print(df.iloc[2])