import pandas as pd
df1=pd.DataFrame({
  'id' :[1,2],
  'name':['john','michael']
})
df2=pd.DataFrame({
  'id':[3,4],
  'age':[23,24]
})
print(pd.concat([df1,df2], ignore_index=True))