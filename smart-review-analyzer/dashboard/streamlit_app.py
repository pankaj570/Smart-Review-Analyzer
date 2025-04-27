import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


import streamlit as st
from app.mcp_controller import run_pipeline

st.title("Smart Review Analyzer")

review = st.text_area("Enter customer review:")

if st.button("Analyze"):
    result = run_pipeline(review)
    st.write("### AI Reply")
    st.success(result['reply'])
    st.write("### Action")
    st.info(result['decision'])
