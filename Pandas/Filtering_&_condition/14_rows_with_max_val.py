import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [90, 60, 90]
})
result = df[df['marks'] == df['marks'].max()]
print("Filtering rows with maximum marks :")
print(result)
print("Filtering rows with minimum marks :")
print(df[df['marks'] == df['marks'].min()])