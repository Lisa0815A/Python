import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🍔 Food Order Analysis Dashboard")

# Load data
df = pd.read_csv("data.csv")

# Convert time
df['time'] = pd.to_datetime(df['time'], format='%H:%M')
df['hour'] = df['time'].dt.hour

# Sidebar filters
st.sidebar.header("Filter Options")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df['category'].unique())
)

# Apply filter
if category != "All":
    df = df[df['category'] == category]

# ==========================
# 📊 1. Hourly Orders
# ==========================
st.subheader("📈 Orders by Hour")

hourly_orders = df.groupby('hour')['order_id'].count()

fig1, ax1 = plt.subplots()
ax1.plot(hourly_orders.index, hourly_orders.values, marker='o')
ax1.set_xlabel("Hour")
ax1.set_ylabel("Orders")

st.pyplot(fig1)

# ==========================
# 📊 2. Orders by Category
# ==========================
st.subheader("📊 Orders by Category")

fig2, ax2 = plt.subplots()
df['category'].value_counts().plot(kind='bar', ax=ax2)
st.pyplot(fig2)

# ==========================
# 💰 3. Revenue by Category
# ==========================
st.subheader("💰 Revenue by Category")

fig3, ax3 = plt.subplots()
df.groupby('category')['price'].sum().plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# ==========================
# 📉 4. Price Distribution
# ==========================
st.subheader("📉 Price Distribution")

fig4, ax4 = plt.subplots()
sns.histplot(df['price'], bins=20, kde=True, ax=ax4)
st.pyplot(fig4)

# ==========================
# 🏆 5. Top Items
# ==========================
st.subheader("🏆 Top Selling Items")

top_items = df['item'].value_counts().head(10)

fig5, ax5 = plt.subplots()
top_items.plot(kind='barh', ax=ax5)
ax5.invert_yaxis()

st.pyplot(fig5)