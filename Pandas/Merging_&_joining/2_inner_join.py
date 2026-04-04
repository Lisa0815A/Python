import pandas as pd
#create two dataframes
df1 = pd.DataFrame({
  'id' : [1,2,3],
  'name' : ['john','michael','susan']
})
df2 = pd.DataFrame({
  'id' : [1,2,4],
  'age' :[23,24,25]
})
inner_join_df = pd.merge(df1,df2,on='id',how='inner')
print("Inner join merged dataframe:")
print(inner_join_df)