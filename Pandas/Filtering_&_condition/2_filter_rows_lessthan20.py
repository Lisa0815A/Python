import pandas as pd
df = pd.DataFrame({
  'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
  'marks' : [15, 22, 18, 30, 12]
})
result = df[df['marks']<20]
print("Filtering rows less than 20 :")
print(result)