from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


MODEL_RESULTS = Path(
    "outputs/results/model_comparison.csv"
)


def show_model_chart():

    st.subheader("📊 Model Comparison")

    if not MODEL_RESULTS.exists():
        st.warning("Model comparison file not found.")
        return

    df = pd.read_csv(MODEL_RESULTS)

    fig = px.bar(
        df,
        x="Model",
        y="R2",
        text="R2",
        title="Model Performance",
    )

    fig.update_layout(
        height=500,
        xaxis_title="",
        yaxis_title="R² Score",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )