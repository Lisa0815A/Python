import pandas as pd
#creating two dataframes
df1 = pd.DataFrame({
  'id1' : [1,2,3],
  'name' : ['john','michael','susan'] 
})
df2 = pd.DataFrame({
  'id2' : [1,2,4],
  'age' : [25,30,28]
})
#merge with different column names
result = pd.merge(df1,df2,left_on = 'id1', right_on = 'id2')
print(result)
