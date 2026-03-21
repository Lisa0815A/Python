import pandas as pd

s = pd.Series([10,20,30])
print("series :\n",s)
df = s.to_frame(name="number")
print("Series to dataframe :\n",df)