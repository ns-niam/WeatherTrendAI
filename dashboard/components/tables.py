from pathlib import Path

import pandas as pd
import streamlit as st


LEADERBOARD = Path(
    "outputs/results/leaderboard.csv"
)


def show_leaderboard():

    st.subheader(" Model Leaderboard")

    if not LEADERBOARD.exists():
        st.warning("Leaderboard not found.")
        return

    df = pd.read_csv(LEADERBOARD)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )