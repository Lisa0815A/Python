import pandas as pd
df = pd.read_csv(r"C:\Users\Lisa\OneDrive\Desktop\Data_Science\Pandas\Practice\data.csv")
print(df)
print("Frequency of values in the price column :")
print(df['price'].value_counts())