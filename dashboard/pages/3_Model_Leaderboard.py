from pathlib import Path
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.visualization.plots import leaderboard_plot


st.set_page_config(
    page_title="Leaderboard",
    page_icon="",
    layout="wide",
)

st.title(" Model Leaderboard")

path = Path("outputs/results/leaderboard.csv")

if not path.exists():

    st.error("leaderboard.csv not found.")

    st.stop()

df = pd.read_csv(path)

st.dataframe(
    df,
    width="stretch",
    hide_index=True,
)

best = df.iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Best Model",
    best["Model"],
)

c2.metric(
    "MAE",
    f'{best["MAE"]:.3f}',
)

c3.metric(
    "RMSE",
    f'{best["RMSE"]:.3f}',
)

c4.metric(
    "R²",
    f'{best["R2"]:.4f}',
)

fig = leaderboard_plot(df)

st.plotly_chart(
    fig,
    width="stretch",
)

st.download_button(
    "⬇ Download Leaderboard",
    df.to_csv(index=False),
    file_name="leaderboard.csv",
    mime="text/csv",
    width="stretch",
)