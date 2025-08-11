import streamlit as st
from config import *

st.set_page_config(page_title=APP_TITLE, layout=PAGE_LAYOUT, page_icon=APP_ICON)

# Create navigation pages
home_page = st.Page("home.py", title="🏠 Home", default=True)
about_page = st.Page("about.py", title="ℹ️ About")  
report_page = st.Page("report.py", title="📊 Reports")      
expense_add_page = st.Page("add_expense.py", title="➕ Add Expense")
budget_page = st.Page("budget.py", title="💰 Budget")
monthly_page = st.Page("monthly.py", title="📅 Monthly Expense Data") 
goals_page = st.Page("goal.py", title="🎯 Goals")
guidelines_page = st.Page("guidelines.py", title="📘 Guidelines")
    
# Create navigation
pg = st.navigation(pages=[home_page, about_page, expense_add_page, budget_page, report_page, monthly_page, goals_page, guidelines_page])

# Enhanced sidebar with quick stats
with st.sidebar:  
    # Quick stats in sidebar
    try:
        from utils import load_cached_expense_data, get_total_balance, format_currency
        df_data = load_cached_expense_data()
        if not df_data.empty:
            total_balance = get_total_balance(df_data)
            st.metric("💰 Total Balance", format_currency(total_balance))
    except:
        pass  
    
    # Quick actions
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Quick Add", use_container_width=True,type="primary"):
            st.switch_page("add_expense.py")
    with col2:
        if st.button("📊 Reports", use_container_width=True,type="primary"):
            st.switch_page("report.py")

    st.markdown("---")
    st.caption(f"© {DEVELOPER_NAME} • All rights reserved")

pg.run()
