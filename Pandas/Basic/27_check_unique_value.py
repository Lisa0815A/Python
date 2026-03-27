import pandas as pd
data = {
    "name": ['lisa', 'bob', 'usha', 'lisa', 'bob']
}

df = pd.DataFrame(data)
print(df['name'].unique())