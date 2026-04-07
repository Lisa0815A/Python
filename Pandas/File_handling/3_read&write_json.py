import pandas as pd
data = pd.DataFrame({
  'name' : ['Alice', 'Bob', 'Charlie'],
  'marks' : [90, 80, 75]
})
data.to_json('students.json', orient='records', lines=True)
df = pd.read_json('students.json', orient='records',lines=True)
print (df)
