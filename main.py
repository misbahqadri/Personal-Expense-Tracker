import streamlit as st

st.set_page_config(page_title=" Expense Tracker", layout="wide",page_icon="💰")

# st.title("💸 Personal Expense Tracker")


# st.logo("images/personal_finance_logo.png")
# st.logo("images/Pi7_Tool_personal_finance_logo (1).png")

# Sidebar layout with categories
# pg = st.navigation(
#     {
#         "🏠 Expenses": [home_page],
#         "📘 Info": [about_page,guidlines_page],
#         "📊 Finance": [tracker_page, monthly_page, report_page],
#         "💡 Planning": [goals_page]
#     }
# )


home_page = st.Page("home.py", title="🏠 Home",default=True)
about_page = st.Page("about.py", title="🙋‍♂️ About Me")     
report_page = st.Page("report.py", title="📊 Reports")      
# tracker_page = st.Page("tracker.py", title="💸 Expense Tracker")
expense_add_page = st.Page("add_expense.py",title="➕ Add Expense")
monthly_page = st.Page("monthly.py", title="📝 Monthly Overview")  # More relevant than 
goals_page = st.Page("goal.py", title="🎯 Goals")
guidlines_page = st.Page("guidlines.py", title="📘 Guidelines")

pg = st.navigation(pages=[home_page,about_page,expense_add_page ,report_page,monthly_page,goals_page,guidlines_page])

with st.sidebar:
    # st.image("https://cdn-icons-png.flaticon.com/512/4290/4290854.png", width=60)
    st.image("images/tracker.gif")

    st.markdown("## 💼 Personal Finance App")
    st.text("By Misbah Qadri")


pg.run()
