import streamlit as st
from config import DEVELOPER_NAME, DEVELOPER_EMAIL, DEVELOPER_GITHUB, APP_TITLE

st.title("ℹ️ About")

st.markdown(r"""
Welcome to the Personal Expense Tracker — a simple, fast, and privacy‑friendly app to help you take control of your money. 
Use it to record transactions, set budgets, and track goals — all on your device.
""")

st.markdown("---")

col1, col2 = st.columns([3, 2])
with col1:
    st.subheader("What you can do")
    st.markdown(r"""
    - Track daily **Income** and **Expense** entries
    - Get clear **reports** (Pie, Bar, Line) to understand spending
    - Set monthly **budgets** and monitor progress
    - Define **financial goals** and watch your progress grow
    - Import from CSV and export your data anytime
    """)
with col2:
    st.subheader("Why you'll like it")
    st.markdown(r"""
    - Clean, focused, and easy to use
    - Data stored locally (CSV) — **you own your data**
    - Works offline for most tasks
    - Lightweight and fast
    """)

st.markdown("---")

st.subheader("Key features at a glance")
feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)
with feat_col1:
    st.markdown("**➕ Add transactions**\n\nSingle entry form + bulk CSV import")
with feat_col2:
    st.markdown("**📊 Visual reports**\n\nCategory split, trends, monthly view")
with feat_col3:
    st.markdown("**💰 Budgets**\n\nSet per‑category monthly limits")
with feat_col4:
    st.markdown("**🎯 Goals**\n\nTrack targets with live progress")

st.markdown("---")

st.subheader("Privacy")
st.markdown(r"""
Your data is saved to local CSV files in the `data/` folder. No servers, no accounts, no cloud. 
You can back up or delete the files at any time.
""")

st.markdown("---")

st.subheader("Technology")
st.markdown(r"""
- **Python**  
- **Streamlit** (UI)  
- **Pandas** (data)  
- **Plotly** (charts)
""")

st.markdown("---")

st.subheader("Developer")
st.markdown(
    f"""
**{DEVELOPER_NAME}**  
📫 Email: [{DEVELOPER_EMAIL}](mailto:{DEVELOPER_EMAIL})  
🔗 GitHub: [https://{DEVELOPER_GITHUB}](https://{DEVELOPER_GITHUB})
"""
)

st.info("Thanks for using the app. Your money, your control. 🌟")
