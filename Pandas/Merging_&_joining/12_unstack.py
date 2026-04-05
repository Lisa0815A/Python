import pandas as pd
df = pd.DataFrame({
  'A':[1,2],
  'B':[3,4]
})
print("stacked dataframe :")
result = df.stack()
print(result)
print("unstacked dataframe :")
unstacked =result.unstack()
print(unstacked)