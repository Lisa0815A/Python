import pandas as pd

data = {
    "age": ['12', '15', '18']
}

df = pd.DataFrame(data)

df['age'] = df['age'].astype(int)

print(df.dtypes)