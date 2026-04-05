import pandas as pd
df = pd.DataFrame({
  'A' : [1,2],
  'B' :[3,4]
})
#stack
#stack -it converts column into rows
result = df.stack()
print(result)