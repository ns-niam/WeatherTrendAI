from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Project Summary",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Project Summary")

path = Path("outputs/reports/summary.txt")

if not path.exists():
    st.error("summary.txt not found.")
    st.stop()

summary = path.read_text()

st.text(summary)