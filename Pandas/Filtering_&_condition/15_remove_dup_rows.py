import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'marks': [90, 60, 90, 75]
})
df = df.drop_duplicates()
print(df)
print("Last occurrence of duplicate rows:")
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'marks': [90, 60, 90, 75]
})
df1 = df1.drop_duplicates(keep='last') 
print(df1) 
print("First occurrence of duplicate rows:")
df2 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'marks': [90, 60, 90, 75]
})
df2 = df2.drop_duplicates(keep='first') 
print(df2) 