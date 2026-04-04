import pandas as pd

df1 = pd.DataFrame({
  'id' :[1,2,3],
  'name':['john','michael','susan']
})
df2 = pd.DataFrame({
  'id' :[1,2,4],
  'age':[23,24,25]
})
#inner join default
merged_df1 = pd.merge(df1,df2,on='id')
print("Inner join default merged dataframe:")
print(merged_df1)
#merge with left join
merged_df2 = pd.merge(df1,df2,on='id',how='left')
print("\n left join merged dataframe:")
print(merged_df2)
#merge with right join
merged_df3 = pd.merge(df1,df2,on='id',how='right')
print("\n right join merged dataframe:")
print(merged_df3)
#merge with outer join
merged_df4 = pd.merge(df1,df2,on='id',how='outer')
print("\n outer join merged dataframe:")
print(merged_df4)