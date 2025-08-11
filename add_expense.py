import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta, date
import plotly.express as px
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError


st.title("💸 Add Expense or Income")

# ----------- CSV Load or Create-----------------
csv_file = os.path.join("data", "add_expense.csv")
os.makedirs("data", exist_ok=True)  # Ensure folder exists

# Load data from CSV or create a new DataFrame
def load_data():
    try:
        return pd.read_csv(csv_file, parse_dates=["Date"])
    except (FileNotFoundError, EmptyDataError):
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Description"])

def save_data(df):
    df.to_csv(csv_file, index=False)

df_data = load_data()
# df_data["Date"] = pd.to_datetime(df_data["Date"])  # ✅ Fix type
df_data["Date"] = pd.to_datetime(df_data["Date"], format='mixed')


tab1, tab2, tab3 = st.tabs(["➕ Add Entry", "📄 Transactions", "📁 Import/Export"])


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
        # filtered_data["Date"] = filtered_data["Date"].dt.date

        submitted = st.form_submit_button("💾 Save Entry")

        if submitted:
            new_entry = pd.DataFrame([{
                "Date": pd.to_datetime(date).date(),
                "Type": entry_type,
                "Category": category,
                "Amount": amount,
                "Description": description
            }])
            df_data = pd.concat([df_data, new_entry], ignore_index=True)
            save_data(df_data)
            st.success("Entry saved successfully!")

with tab2:
    # st.subheader("📌 Recent Transactions")
    
    if df_data.empty:
        st.info("No transactions yet. Start by adding one above.")
    else:
        # --- Filter Options ---
        st.markdown("### 🗂️ Filter By")
        filter_option = st.radio(
            "Select filter:",
            ["This Week", "This Month", "This Year", "Custom Range"],
            horizontal=True
        )

        today = datetime.now()

        if filter_option == "This Week":
            start_date = today - timedelta(days=today.weekday())
            end_date = today

        elif filter_option == "This Month":
            start_date = today.replace(day=1)
            end_date = today

        elif filter_option == "This Year":
            start_date = today.replace(month=1, day=1)
            end_date = today

        elif filter_option == "Custom Range":
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("From", value=today.replace(day=1))
            with col2:
                end_date = st.date_input("To", value=today)

        if start_date > end_date:
            st.error("⚠️ Start date cannot be after end date.")
        else:
            # Normalize comparisons to date-only to avoid Timestamp vs date issues
            start_cmp = pd.to_datetime(start_date).date()
            end_cmp = pd.to_datetime(end_date).date()
            date_series = pd.to_datetime(df_data["Date"], errors="coerce").dt.date

            mask = (date_series >= start_cmp) & (date_series <= end_cmp)
            filtered_data = df_data.loc[mask].sort_values(by="Date", ascending=False)

            if filtered_data.empty:
                st.info(f"No transactions from {start_date} to {end_date}")
            else:
                # Convert datetime to date only and hide index
                display_data = filtered_data.copy()
                display_data["Date"] = display_data["Date"].dt.date
                # Simple inline edit/delete controls
                st.dataframe(display_data, use_container_width=True, hide_index=True)

                # Inline delete by selecting an index from filtered view
                delete_idx = st.selectbox("Select a row to delete (by index)", options=filtered_data.index.tolist(), format_func=lambda i: f"{filtered_data.loc[i, 'Date'].date()} | {filtered_data.loc[i, 'Category']} | ₹{filtered_data.loc[i, 'Amount']}" if 'Date' in filtered_data.columns else str(i))
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("🗑️ Delete Selected"):
                        df_data.drop(index=delete_idx, inplace=True)
                        df_data.reset_index(drop=True, inplace=True)
                        save_data(df_data)
                        st.success("✅ Deleted successfully!")
                        st.rerun()
                with col_b:
                    st.caption("Edit coming soon (amount/category/date)")

                # Download button
                csv = filtered_data.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Filtered Transactions (CSV)",
                    data=csv,
                    file_name=f"transactions_{start_date}_to_{end_date}.csv",
                    mime='text/csv'
                )

# --------------- TAB 3: Import/Export ----------------
with tab3:
    st.subheader("📁 Import/Export Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📥 Download Sample CSV")
        st.markdown("Download a sample CSV file with the correct format to add multiple expenses at once.")
        
        # Create sample data
        sample_data = pd.DataFrame({
            "Date": ["2025-01-15", "2025-01-16", "2025-01-17"],
            "Type": ["Expense", "Income", "Expense"],
            "Category": ["Food", "Salary", "Transport"],
            "Amount": [500.0, 50000.0, 200.0],
            "Description": ["Lunch at restaurant", "Monthly salary", "Bus fare"]
        })
        
        csv_sample = sample_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Sample CSV",
            data=csv_sample,
            file_name="sample_expenses.csv",
            mime="text/csv",
            help="Download a sample CSV file with the correct format"
        )
        
        st.markdown("""
        **CSV Format:**
        - Date: YYYY-MM-DD format
        - Type: "Income" or "Expense"
        - Category: Any category name
        - Amount: Numeric value
        - Description: Optional text
        """)
    
    with col2:
        st.markdown("### 📤 Upload & Merge CSV")
        st.markdown("Upload a CSV file to add multiple expenses at once. The data will be merged with existing records.")
        
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload a CSV file with expense/income data"
        )
        
        if uploaded_file is not None:
            try:
                # Read uploaded file
                uploaded_df = pd.read_csv(uploaded_file)
                
                # Validate required columns
                required_columns = ["Date", "Type", "Category", "Amount"]
                missing_columns = [col for col in required_columns if col not in uploaded_df.columns]
                
                if missing_columns:
                    st.error(f"❌ Missing required columns: {', '.join(missing_columns)}")
                    st.error("Please ensure your CSV has: Date, Type, Category, Amount columns")
                else:
                    # Show preview of uploaded data
                    st.markdown("### 📋 Preview of Uploaded Data")
                    
                    # Convert date column to datetime for display
                    display_df = uploaded_df.copy()
                    if "Date" in display_df.columns:
                        display_df["Date"] = pd.to_datetime(display_df["Date"], errors="coerce")
                        display_df["Date"] = display_df["Date"].dt.date
                    
                    st.dataframe(display_df, use_container_width=True, hide_index=True)
                    
                    # Show summary
                    total_rows = len(uploaded_df)
                    total_amount = uploaded_df["Amount"].sum()
                    income_count = len(uploaded_df[uploaded_df["Type"] == "Income"])
                    expense_count = len(uploaded_df[uploaded_df["Type"] == "Expense"])
                    
                    st.markdown("### 📊 Upload Summary")
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Total Records", total_rows)
                    col2.metric("Total Amount", f"₹ {total_amount:,.2f}")
                    col3.metric("Income Records", income_count)
                    col4.metric("Expense Records", expense_count)
                    
                    # Merge button
                    if st.button("🔄 Merge with Existing Data", type="primary"):
                        try:
                            # Validate and clean data
                            cleaned_df = uploaded_df.copy()
                            
                            # Convert date to datetime
                            cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"], errors="coerce")
                            
                            # Remove rows with invalid dates
                            invalid_dates = cleaned_df["Date"].isna().sum()
                            if invalid_dates > 0:
                                st.warning(f"⚠️ {invalid_dates} rows with invalid dates will be skipped")
                                cleaned_df = cleaned_df.dropna(subset=["Date"])
                            
                            # Validate amounts
                            cleaned_df["Amount"] = pd.to_numeric(cleaned_df["Amount"], errors="coerce")
                            invalid_amounts = cleaned_df["Amount"].isna().sum()
                            if invalid_amounts > 0:
                                st.warning(f"⚠️ {invalid_amounts} rows with invalid amounts will be skipped")
                                cleaned_df = cleaned_df.dropna(subset=["Amount"])
                            
                            # Remove zero amounts
                            zero_amounts = len(cleaned_df[cleaned_df["Amount"] == 0])
                            if zero_amounts > 0:
                                st.warning(f"⚠️ {zero_amounts} rows with zero amounts will be skipped")
                                cleaned_df = cleaned_df[cleaned_df["Amount"] != 0]
                            
                            # Validate types
                            valid_types = ["Income", "Expense"]
                            invalid_types = cleaned_df[~cleaned_df["Type"].isin(valid_types)]
                            if len(invalid_types) > 0:
                                st.warning(f"⚠️ {len(invalid_types)} rows with invalid types will be skipped")
                                cleaned_df = cleaned_df[cleaned_df["Type"].isin(valid_types)]
                            
                            # Clean categories (remove empty ones)
                            cleaned_df = cleaned_df.dropna(subset=["Category"])
                            cleaned_df = cleaned_df[cleaned_df["Category"] != ""]
                            
                            # Ensure description column exists
                            if "Description" not in cleaned_df.columns:
                                cleaned_df["Description"] = ""
                            
                            # Merge with existing data
                            if not cleaned_df.empty:
                                # Convert date to date only for consistency
                                cleaned_df["Date"] = cleaned_df["Date"].dt.date
                                
                                # Merge with existing data
                                prev_count = len(df_data)
                                merged_df = pd.concat([df_data, cleaned_df], ignore_index=True)
                                
                                # Remove duplicates based on all columns
                                initial_count = len(merged_df)
                                merged_df = merged_df.drop_duplicates()
                                duplicates_removed = initial_count - len(merged_df)
                                
                                if duplicates_removed > 0:
                                    st.info(f"ℹ️ {duplicates_removed} duplicate records were automatically removed")
                                
                                # Save merged data
                                save_data(merged_df)

                                # Verify by reloading from disk
                                try:
                                    verified_df = load_data()
                                except Exception:
                                    verified_df = merged_df

                                # Show success message and details
                                st.success(f"✅ Successfully merged {len(cleaned_df)} valid records!")
                                st.info(f"ℹ️ Duplicates removed: {duplicates_removed}")
                                st.success(f"📊 Total records before: {prev_count} → after: {len(verified_df)}")

                                # Show a preview of merged data
                                st.markdown("### 📄 Merged Data Preview (latest 20)")
                                preview_df = verified_df.copy()
                                preview_df["Date"] = pd.to_datetime(preview_df["Date"], errors="coerce").dt.date
                                preview_df = preview_df.sort_values("Date", ascending=False).head(20)
                                st.dataframe(preview_df, use_container_width=True, hide_index=True)

                                # Optional: refresh page so other tabs pick up new data
                                if st.button("🔄 Refresh page to load latest data"):
                                    st.rerun()
                            else:
                                st.error("❌ No valid records found in the uploaded file")
                                
                        except Exception as e:
                            st.error(f"❌ Error merging data: {str(e)}")
                            st.error("Please check your CSV format and try again")
                
            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")
                st.error("Please ensure you're uploading a valid CSV file")
    
    # Additional help
    st.markdown("---")
    st.markdown("### 💡 Tips for CSV Import")
    st.markdown("""
    - **Date Format**: Use YYYY-MM-DD (e.g., 2025-01-15)
    - **Type**: Must be exactly "Income" or "Expense"
    - **Amount**: Use numbers only (e.g., 500.50)
    - **Category**: Any text (e.g., Food, Salary, Transport)
    - **Description**: Optional text (can be left empty)
    - **Headers**: First row should contain column names
    """)
