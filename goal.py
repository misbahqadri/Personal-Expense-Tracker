# goals.py
import streamlit as st

st.title("🎯 Financial Goals")

goal = st.text_input("Your Goal (e.g. Save for vacation)")
target_amount = st.number_input("Target Amount", min_value=0.0, step=100.0)
amount_saved = st.number_input("Amount Saved", min_value=0.0, step=100.0)

if target_amount > 0:
    progress = min(amount_saved / target_amount, 1.0)
    st.progress(progress, text=f"{progress*100:.1f}% completed")

