from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Leaderboard",
    page_icon="",
    layout="wide",
)

st.title("Model Leaderboard")

path = Path("outputs/results/leaderboard.csv")

if not path.exists():

    st.error("leaderboard.csv not found.")

    st.stop()

df = pd.read_csv(path)

st.dataframe(
    df,
    width="stretch",
)

best = df.iloc[0]

st.metric(
    "Best Model",
    best["Model"],
)

st.metric(
    "R²",
    f'{best["R2"]:.4f}',
)

st.download_button(
    "Download Leaderboard",
    df.to_csv(index=False),
    file_name="leaderboard.csv",
    mime="text/csv",
    width="stretch",
)