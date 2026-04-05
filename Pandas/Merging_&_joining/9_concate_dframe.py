import pandas as pd
df1 = pd.DataFrame({
  'name' : ['john','mary','peter'],
  'id': [1,2,3]
})
df2 = pd.DataFrame({
  'age' : [23,24,25],
  'id':[1,2,4]
})
#concatenating datafraame
concate_dframe = pd.concat([df1,df2])
print(concate_dframe)