import pandas as pd
data = {
    "name": ['lisa','bob','usha','bichi','pabi'],
    "department": ['IT','HR','IT','HR','IT'],
    "salary": [50000,40000,60000,45000,70000]
}
df = pd.DataFrame(data)
print(df.groupby('department').count())