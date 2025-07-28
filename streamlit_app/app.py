import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/aggregated_transaction.csv")

st.set_page_config(layout="wide")
st.title("📊 PhonePe Transaction Insights")

year = st.selectbox("Select Year", sorted(df['year'].unique()))
quarter = st.selectbox("Select Quarter", sorted(df['quarter'].unique()))
selected = df[(df['year'] == year) & (df['quarter'] == quarter)]

st.subheader("Total Transaction Amount by State")
state_wise = selected.groupby("state")["amount"].sum().sort_values(ascending=False)
st.bar_chart(state_wise)

st.subheader("Transaction Type Distribution")
type_dist = selected.groupby("transaction_type")["amount"].sum()
fig, ax = plt.subplots()
type_dist.plot(kind="pie", autopct='%1.1f%%', ax=ax)
st.pyplot(fig)
