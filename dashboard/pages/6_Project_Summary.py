from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Project Summary",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Project Summary")

st.caption(
    "Summary of the WeatherTrendAI project, methodology, model performance, and key outcomes."
)

path = Path("outputs/reports/summary.txt")

if not path.exists():
    st.error("❌ summary.txt not found.")
    st.stop()

summary = path.read_text()

st.info(
    """
This report summarizes the complete WeatherTrendAI pipeline,
including data preprocessing, feature engineering, model training,
evaluation, forecasting, and final results.
"""
)

st.divider()

st.markdown("### 📋 Project Report")

st.code(
    summary,
    language="text",
)

st.download_button(
    "⬇ Download Summary",
    data=summary,
    file_name="WeatherTrendAI_Summary.txt",
    mime="text/plain",
    width="stretch",
)

st.divider()

st.success("✅ Report generated successfully.")