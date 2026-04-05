import pandas as pd
df = pd.DataFrame({
    'name': ['john', 'mary', 'john'],
    'id':[1,2,1]
})
print("DataFrame :")
print(df)
remove_dup = df.drop_duplicates()
print("DataFrame after removing duplicates :")
print(remove_dup)