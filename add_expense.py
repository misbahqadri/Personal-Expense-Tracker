import streamlit as st
import pandas as pd
from datetime import datetime

st.title("💸 Add Expense or Income")
st.markdown("Use the form below to add your financial transactions.")


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

tab1, tab2 = st.tabs(["➕ Add Entry"," 📄 Transactions"])

with tab1: 
    with st.form("entry_form", clear_on_submit=True):
        st.subheader("➕ Add New Entry")
        col1, col2 = st.columns(2)
        entry_type = col1.selectbox("Type", ["Income", "Expense"])
        category = col2.selectbox("Category", ["Salary", "Food", "Transport", "Shopping", "Bills", "Others"])

        col3, col4 = st.columns(2)        
        amount = col3.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        date = col4.date_input("Date", value=datetime.now().date())
        description = st.text_input("Description (optional)")

        submitted = st.form_submit_button("💾 Save Entry")   
            
        if submitted:
            new_entry = pd.DataFrame([{
                    "Date": pd.to_datetime(date),
                    "Type": entry_type,
                    "Amount": amount,
                    "Category": category,
                    "Description": description
                }])
            df_data = pd.concat([df_data, new_entry], ignore_index=True)
            save_data(df_data)
            st.success("Entry saved successfully!")

with tab2:
    st.subheader("📌 Recent Transactions")

    col1,col2 = st.columns(2)

    # Date range selector
    with col1:
        start_date = st.date_input("From", pd.to_datetime("today").replace(day=1))
    
    with col2:
        end_date = st.date_input("To", pd.to_datetime("today"))

    
    if start_date > end_date:
        st.error("⚠️ Start date cannot be after end date.")
    else:
        # Filter by date
        mask = (df_data['Date'] >= pd.to_datetime(start_date)) & (df_data['Date'] <= pd.to_datetime(end_date))
        filtered_data = df_data.loc[mask].sort_values(by="Date", ascending=False)
        

        st.dataframe(filtered_data, use_container_width=True)

        # Download filtered data
        csv = filtered_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Transactions (CSV)",
            data=csv,
            file_name=f"transactions_{start_date}_to_{end_date}.csv",
            mime='text/csv'
        )
    # st.subheader(" Transactions")
   
    # if not df_data.empty:
    #     recent_data = df_data.sort_values(by="Date", ascending=False).head(10)
    #     st.dataframe(recent_data, use_container_width=True)
    # else:
    #     st.info("No transactions yet. Start by adding one above.")

