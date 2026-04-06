import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'marks': [90, 60, 75, 40],
    'city': ['Chennai', 'Mumbai', 'Delhi', 'Chennai']
})
result1=df[(df['marks'] > 70) & (df['city'] == 'Chennai')]
print(result1)
result2=df[(df['marks'] < 50) | (df['city'] == 'Delhi')]
print(result2)
result3=df.loc[(df['marks'] < 50) & (df['city'] == 'Chennai'), 'marks'] = 0
print(result3)
result4=df.query("marks > 70 and city == 'Chennai'")
print(result4)
result5=df[(df['city'].isin(['Chennai', 'Delhi'])) & (df['marks'] > 70)]
print(result5)