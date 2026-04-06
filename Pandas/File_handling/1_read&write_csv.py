import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [90, 80, 75]
}
df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)
df = pd.read_csv('students.csv')
print(df)