import pandas as pd
df = pd.DataFrame({
  'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
  'age' : [25, 30, 35, 40, 45],
  'marks' : [15, 22, 18, 30, 12]
})
result = df[(df['age']>30) & (df['marks']<20)]
print("Filtering rows with multiple conditions :")
print(result)
#OR operators
result_or = df[(df['marks'] > 70) | (df['age'] < 21)]
print("Filtering rows with OR conditions :")
print(result_or)
#Not operator
result_not = df[~(df['marks'] > 50)]
print("Filtering rows with NOT condition :")
print(result_not)