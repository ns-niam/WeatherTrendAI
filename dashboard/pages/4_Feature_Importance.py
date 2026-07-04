from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Feature Importance",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Feature Importance")

path = Path("outputs/results/feature_importance.csv")

if not path.exists():
    st.error("feature_importance.csv not found.")
    st.stop()

df = pd.read_csv(path)

st.dataframe(
    df,
    width="stretch",
    hide_index=True,
)

fig = px.bar(
    df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Feature Importance",
)

fig.update_layout(
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(
    fig,
    width="stretch",
)