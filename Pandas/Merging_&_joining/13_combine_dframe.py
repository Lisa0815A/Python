import pandas as pd

df1 = pd.DataFrame({
    'name': ['john', 'mary'],
    'id': [1, 2]
})

df2 = pd.DataFrame({
    'name': ['peter', 'lisa'],
    'id': [3, 4]
})

result = pd.concat([df1, df2], ignore_index=True)
print(result)