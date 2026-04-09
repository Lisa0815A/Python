import pandas as pd
import os
print(os.getcwd())
df = pd.read_csv(r"C:\Users\Lisa\OneDrive\Desktop\Data_Science\Pandas\Practice\data.csv")
print(df)
print("Top five highest value :")
print(df.nlargest(5,'price'))
