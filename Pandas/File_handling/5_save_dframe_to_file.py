import pandas as pd
df = pd.DataFrame({
  'name' :[ 'Alice', 'Bob', 'Charlie'],
  'marks' : [90, 80, 75]
})
df.to_csv('marks.csv',index=False)