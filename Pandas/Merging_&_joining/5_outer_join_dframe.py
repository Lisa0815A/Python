import pandas as pd
df1 = pd.DataFrame({
  'id' :[1,2,3],
  'name':['john','michael','susan']
})
df2 = pd.DataFrame({
  'id' :[1,2,4],
  'age':[23,24,25]  
})
outer_join_df = pd.merge(df1,df2,on='id',how='outer')
print("outer join merged dataframe:")
print(outer_join_df)
