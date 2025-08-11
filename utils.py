import streamlit as st
import pandas as pd
import os
import re
import shutil
from datetime import datetime, timedelta
from pandas.errors import EmptyDataError
from config import *

# Data loading and saving functions
def load_expense_data():
    """Load expense data from CSV with proper error handling"""
    try:
        df = pd.read_csv(EXPENSE_FILE)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.dropna(subset=["Date"])  # Remove invalid date rows
        return df
    except (FileNotFoundError, EmptyDataError):
        return pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Description"])

def save_expense_data(df):
    """Save expense data to CSV"""
    df.to_csv(EXPENSE_FILE, index=False)

def load_goals_data():
    """Load goals data from CSV"""
    try:
        return pd.read_csv(GOALS_FILE, parse_dates=["Deadline"])
    except (FileNotFoundError, EmptyDataError):
        return pd.DataFrame(columns=["Goal", "Target Amount", "Amount Saved", "Deadline"])

def save_goals_data(df):
    """Save goals data to CSV"""
    df.to_csv(GOALS_FILE, index=False)

# Validation functions
def validate_amount(amount):
    """Validate amount input"""
    try:
        amount = float(amount)
        return MIN_AMOUNT <= amount <= MAX_AMOUNT
    except (ValueError, TypeError):
        return False

def validate_category(category):
    """Validate category input"""
    if not category or not str(category).strip():
        return False
    return len(str(category).strip()) <= 50

def validate_description(description):
    """Validate description input"""
    if description is None:
        return True  # Description is optional
    return len(str(description)) <= MAX_DESCRIPTION_LENGTH

def sanitize_input(text):
    """Remove potentially harmful characters"""
    if text is None:
        return ""
    return re.sub(r'[<>"\']', '', str(text))

def validate_entry(amount, category, description=""):
    """Validate complete entry"""
    errors = []
    
    if not validate_amount(amount):
        errors.append(f"Amount must be between {MIN_AMOUNT} and {MAX_AMOUNT}")
    
    if not validate_category(category):
        errors.append("Category is required and must be less than 50 characters")
    
    if not validate_description(description):
        errors.append(f"Description must be less than {MAX_DESCRIPTION_LENGTH} characters")
    
    return errors

# Data analysis functions
def get_monthly_summary(df, year, month):
    """Get monthly summary for specific year and month"""
    filtered_df = df[(df["Date"].dt.year == year) & (df["Date"].dt.month == month)]
    
    income = filtered_df[filtered_df["Type"] == "Income"]["Amount"].sum()
    expense = filtered_df[filtered_df["Type"] == "Expense"]["Amount"].sum()
    net = income - expense
    
    return {
        "income": income,
        "expense": expense,
        "net": net,
        "transactions": len(filtered_df)
    }

def get_total_balance(df):
    """Calculate total balance (income - expenses)"""
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()
    return income - expense

def get_top_spending_category(df, months=1):
    """Get top spending category for the last N months"""
    cutoff_date = datetime.now() - timedelta(days=30*months)
    recent_df = df[df["Date"] >= cutoff_date]
    expense_df = recent_df[recent_df["Type"] == "Expense"]
    
    if expense_df.empty:
        return "No expenses"
    
    top_category = expense_df.groupby("Category")["Amount"].sum().idxmax()
    return top_category

def get_average_daily_spending(df, days=30):
    """Calculate average daily spending"""
    cutoff_date = datetime.now() - timedelta(days=days)
    recent_df = df[df["Date"] >= cutoff_date]
    expense_df = recent_df[recent_df["Type"] == "Expense"]
    
    if expense_df.empty:
        return 0
    
    total_expense = expense_df["Amount"].sum()
    return total_expense / days

# Backup functions
def create_backup():
    """Create automatic backup of data files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Backup expense file
    if os.path.exists(EXPENSE_FILE):
        backup_expense = f"{BACKUP_DIR}/expenses_backup_{timestamp}.csv"
        shutil.copy2(EXPENSE_FILE, backup_expense)
    
    # Backup goals file
    if os.path.exists(GOALS_FILE):
        backup_goals = f"{BACKUP_DIR}/goals_backup_{timestamp}.csv"
        shutil.copy2(GOALS_FILE, backup_goals)
    
    return timestamp

def cleanup_old_backups(keep_days=30):
    """Remove backups older than specified days"""
    cutoff_time = datetime.now() - timedelta(days=keep_days)
    
    for filename in os.listdir(BACKUP_DIR):
        filepath = os.path.join(BACKUP_DIR, filename)
        if os.path.isfile(filepath):
            file_time = datetime.fromtimestamp(os.path.getctime(filepath))
            if file_time < cutoff_time:
                os.remove(filepath)

# UI helper functions
def format_currency(amount):
    """Format amount as currency"""
    return f"{CURRENCY} {amount:,.2f}"

def create_metric_card(title, value, delta=None, delta_color="normal"):
    """Create a styled metric card"""
    st.metric(
        label=title,
        value=format_currency(value),
        delta=format_currency(delta) if delta else None,
        delta_color=delta_color
    )

def show_success_message(message):
    """Show success message with consistent styling"""
    st.success(f"✅ {message}")

def show_error_message(message):
    """Show error message with consistent styling"""
    st.error(f"❌ {message}")

def show_warning_message(message):
    """Show warning message with consistent styling"""
    st.warning(f"⚠️ {message}")

def show_info_message(message):
    """Show info message with consistent styling"""
    st.info(f"ℹ️ {message}")

# Caching decorators
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_cached_expense_data():
    """Cached version of load_expense_data"""
    return load_expense_data()

@st.cache_data(ttl=1800)  # Cache for 30 minutes
def get_cached_monthly_summary(year, month):
    """Cached monthly summary calculation"""
    df = load_cached_expense_data()
    return get_monthly_summary(df, year, month)
