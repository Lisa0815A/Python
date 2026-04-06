import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [90, None, 75]
})
result = df[df['marks'].notnull()]
print("Filtering rows with non-null values in marks :")
print(result)