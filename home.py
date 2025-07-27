import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



# st.title("💰 Welcome to Your Personal Finance Tracker")
st.title("💸 Personal Finance Tracker")
# st.caption("Track, plan, and manage your money with ease.")

# st.markdown(f"👋 Hello Lisa! Here's your financial summary for **{datetime.today():%B %Y}**.")

col1,col2,col3 = st.columns([2,1,1])
with col1:
    st.markdown(
        "<div style='text-align:center;color:green;font-size:17px'>"
        "<i>"
        "Track your income, expenses, and goals all in one place."
        "</i>"
        "</div>",
        unsafe_allow_html=True)

with col2: 
    if st.button("💸 Add Expenses ",type="tertiary",use_container_width=True):
        st.switch_page("add_expense.py")

with col3:
    if st.button("📊 Check Reports",type="tertiary", use_container_width=True):
        st.switch_page("report.py")

# ---------- CSV FILE SETUP ----------
csv_file = "add_expense.csv"

# Load data from CSV or create a new DataFrame
def load_data():
    try:
        return pd.read_csv(csv_file, parse_dates=["Date"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Description"])

def save_data(df):
    df.to_csv(csv_file, index=False)

df_data = load_data()

# ---------- SUMMARY METRICS ----------
total_income = df_data[df_data["Type"] == "Income"]["Amount"].sum()
total_expenses = df_data[df_data["Type"] == "Expense"]["Amount"].sum()
net_savings = total_income - total_expenses

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Income", f"₹ {total_income:.2f}")
col2.metric("💸 Total Expenses", f"₹ {total_expenses:.2f}")
col3.metric("📈 Net Savings", f"₹ {net_savings:.2f}")

# st.divider()




# LINE CHART
line_data = df_data.groupby("Date")["Amount"].sum().reset_index()
fig_line = px.line(line_data, x="Date", y="Amount", title="Cash Flow Over Time")
st.plotly_chart(fig_line, use_container_width=True)


st.caption("Need help? Check out the Guidelines page 📘.")

