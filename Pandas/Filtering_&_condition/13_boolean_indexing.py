import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [90, 60, 75]
})
result = df[df['marks'] > 70]
print("Filtering rows where marks are greater than 70 :")
print(result)