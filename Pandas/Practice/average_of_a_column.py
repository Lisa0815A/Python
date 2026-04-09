import pandas as pd
df = pd.read_csv(r"C:\Users\Lisa\OneDrive\Desktop\Data_Science\Pandas\Practice\data.csv")
print(df)
print("Average of price column :")
print(df['price'].mean())