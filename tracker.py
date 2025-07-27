import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ---------- CSV FILE SETUP ----------
csv_file = "transactions.csv"

# Load data from CSV or create a new DataFrame
def load_data():
    try:
        return pd.read_csv(csv_file, parse_dates=["Date"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Description"])

def save_data(df):
    df.to_csv(csv_file, index=False)

# ---------- PAGE SETUP ----------
# st.set_page_config(page_title="Personal Finance Tracker", layout="wide")
st.title("📊 Personal Finance Dashboard")

df_data = load_data()

# # ---------- SUMMARY METRICS ----------
# total_income = df_data[df_data["Type"] == "Income"]["Amount"].sum()
# total_expenses = df_data[df_data["Type"] == "Expense"]["Amount"].sum()
# net_savings = total_income - total_expenses

# col1, col2, col3 = st.columns(3)
# col1.metric("💰 Total Income", f"₹ {total_income:.2f}")
# col2.metric("💸 Total Expenses", f"₹ {total_expenses:.2f}")
# col3.metric("📈 Net Savings", f"₹ {net_savings:.2f}")

st.divider()