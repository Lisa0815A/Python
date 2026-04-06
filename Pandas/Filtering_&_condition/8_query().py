import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [90, 60, 75]
})
result = df.query('marks>70')
print("Filtering rows where marks are greater than 70 using query() :")
print(result)