# monthly.py
import streamlit as st
import pandas as pd

st.title("📅 Monthly Overview")


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

if not df_data.empty:
    st.text("No transactions")


# ----------- SELECT YEAR ------------
years_available = df_data["Date"].dt.year.unique()
selected_year = st.selectbox("📅 Select Year for Monthly Summary", sorted(years_available, reverse=True))

# Filter data for selected year
year_data = df_data[df_data["Date"].dt.year == selected_year]
year_data["Month"] = year_data["Date"].dt.month_name()

# ----------- MONTHLY DISPLAY CARDS ------------
st.subheader(f"Monthly Summary Cards for {selected_year}")

month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

card_style = """
<style>
.card {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin: 10px 5px;
    text-align: center;
}
.card-title {
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 10px;
    color: #2b7cff;
}
.card-value {
    font-size: 16px;
    margin: 2px 0;
}
</style>
"""

st.markdown(card_style, unsafe_allow_html=True)

for i in range(0, 12, 3):  # Show in 3-column layout
    cols = st.columns(3)
    for j in range(3):
        if i + j < 12:
            month = month_order[i + j]
            month_df = year_data[year_data["Month"] == month]
            income = month_df[month_df["Type"] == "Income"]["Amount"].sum()
            expense = month_df[month_df["Type"] == "Expense"]["Amount"].sum()
            net = income - expense

            card_html = f"""
                <div class='card'>
                    <div class='card-title'>📅 {month}</div>
                    <div class='card-value'>💰 Income: ₹ {income:.2f}</div>
                    <div class='card-value'>💸 Expense: ₹ {expense:.2f}</div>
                    <div class='card-value'>📈 Net: ₹ {net:.2f}</div>
                </div>
            """
            cols[j].markdown(card_html, unsafe_allow_html=True)
