import pandas as pd
df = pd.DataFrame({
  'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
  'marks' : [15, 22, 18, 30, 12],
  'grade' : ['A', 'B', 'A', 'C', 'B'],
  'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
result = df[df['grade'].isin(['A','B'])]
print("Filtering rows where grade is A or B :")
print(result)