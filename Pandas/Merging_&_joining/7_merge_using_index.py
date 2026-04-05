import pandas as pd
df1 = pd.DataFrame({
  'name': ['john','mary','peter']  
},index = [1,2,3])
df2 = pd.DataFrame({
  'age' : [23,24,25]
},index = [1,2,4])
#merging using index
merging_index = pd.merge(df1,df2,left_index=True,right_index=True,how='inner')
print(merging_index)