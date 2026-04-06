import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'marks': [90, 60, 90, 75]
})
df = df.drop_duplicates()
print(df)