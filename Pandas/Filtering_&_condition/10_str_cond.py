import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'city': ['Chennai', 'Mumbai', 'Delhi', 'Chennai']
})
result = df[df['name'].str.contains('a',case=False)]
print(result)
result1 = df[df['name'].str.startswith('A')]
print("It show the result which starting with A :")
print(result1)
print("It show the result which ending with e :")
result2 = df[df['name'].str.endswith('e')]
print(result2)
print("It show the result which is exactly matching :")
result3 = df[df['city'] == 'Chennai']
print(result3)
result4 = df[df['name'].str.contains('a') & df['city'].str.contains('Chennai')]
print("It shows the result which contains a with city name chennai ")
print(result4)