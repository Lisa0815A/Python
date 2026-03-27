import pandas as pd
data = {
  "name": ['lisa','bob','usha','bichi','pabi'],
  "department": ['IT','HR','IT','HR','IT'],
  "city": ['BBSR','Delhi','BBSR','Delhi','Mumbai'],
  "salary": [50000,40000,60000,45000,70000]
}
df = pd.DataFrame(data)
df['salary_doubled'] = df['salary'].apply(lambda x: x*2)
print(df)