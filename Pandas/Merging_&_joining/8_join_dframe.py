import pandas as pd
df1 = pd.DataFrame({
  'name' : ['john','mary','susan']
},index=[1,2,3])
df2 = pd.DataFrame({
  'age' : [23,24,25]
},index = [1,2,4])
#joining using index
joining_index = df1.join(df2)
print(joining_index)