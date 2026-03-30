import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv("data.csv")

print("First 5 rows:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nShape:", df.shape)

# 2. Data Cleaning
print("\nMissing values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

# 3. Feature Engineering
# -------------------------------
df['time'] = pd.to_datetime(df['time'], format='%H:%M')
df['hour'] = df['time'].dt.hour
hourly_orders = df.groupby('hour')['order_id'].count()

# 4. Analysis
# Rush hours
rush_hours = df.groupby('hour').size().sort_values(ascending=False)
print("\nRush Hours:\n", rush_hours)

# Most popular item
popular_item = df['item'].value_counts()
print("\nMost Popular Items:\n", popular_item)

# Revenue
total_revenue = df['price'].sum()
print("\nTotal Revenue:", total_revenue)

# Average order value
avg_order = np.mean(df['price'])
print("Average Order Value:", avg_order)

# Category-wise revenue
category_sales = df.groupby('category')['price'].sum().sort_values(ascending=False)
print("\nCategory-wise Revenue:\n", category_sales)

# 5. Visualization
# Graph 01: Hourly order 
sns.set_style("whitegrid")
plt.figure(figsize=(12,6))
plt.plot(hourly_orders.index, hourly_orders.values,
         color='teal', marker='o', linewidth=2, markersize=6)
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
# Titles & labels
plt.title("Hourly Order Trend", fontsize=16, fontweight='bold')
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Number of Orders", fontsize=12)

# Grid
plt.grid(True, linestyle='--', alpha=0.6)

# Highlight peak hour 🔥
peak_hour = hourly_orders.idxmax()
peak_value = hourly_orders.max()

plt.scatter(peak_hour, peak_value, color='red', s=100)
plt.annotate("Peak demand (Evening)",  
  xy = (peak_hour,peak_value),
  xytext=(peak_hour+1, peak_value+5),
  arrowprops=dict(arrowstyle="->",color="black"),
  fontsize=10
)

# Remove extra borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xticks(range(0,24))  # show all hours

plt.tight_layout()
plt.show()
#Graph 02:orders by category
plt.figure(figsize=(8,5))

cat_counts = df['category'].value_counts()

cat_counts.plot(
    kind='bar', color='skyblue', edgecolor='black'
)

top_cat = cat_counts.idxmax()
top_val = cat_counts.max()

plt.text(0, top_val,
         f"Top: {top_cat}",
         fontsize=10, color='black')

plt.title("Orders by Category", fontsize=14, fontweight='bold')
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()
#Graph 03:Revenue by category
plt.figure(figsize=(8,5))

rev = df.groupby('category')['price'].sum()

rev.plot(
    kind='bar', color='orange', edgecolor='black'
)

top_rev_cat = rev.idxmax()
top_rev_val = rev.max()

plt.text(0, top_rev_val,
         f"Highest: {top_rev_cat}",
         fontsize=10)

plt.title("Revenue by Category", fontsize=14, fontweight='bold')
plt.xlabel("Category")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()
#Graph 04:price distribution
plt.figure(figsize=(8,5))

plt.hist(df['price'], bins=20, color='purple', alpha=0.7)

plt.title("Price Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.grid(True, linestyle='--', alpha=0.6)
mean_price = df['price'].mean()

plt.axvline(mean_price, color='red', linestyle='--')

plt.text(mean_price, plt.ylim()[1]*0.8,
         "Average Price",
         color='red')

plt.show()
#Graph 05:Top items selling
plt.figure(figsize=(8,5))

top_items = df['item'].value_counts().head(10)

top_items.plot(
    kind='barh', color='teal', edgecolor='black'
)

top_item = top_items.idxmax()
top_value = top_items.max()

plt.text(top_value, 0,
         f"Top: {top_item}",
         fontsize=10)

plt.title("Top 10 Selling Items", fontsize=14, fontweight='bold')
plt.xlabel("Number of Orders")
plt.ylabel("Item")

plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.show()
# 6. Insights
# -------------------------------
print("\n--- INSIGHTS ---")
print("• Peak rush hours occur during lunch and evening times.")
print("• The most ordered food item reflects customer preference.")
print("• Fast food category generates the highest revenue.")
print("• Evening sales are higher compared to morning.")
print("• Average order value shows moderate customer spending.")