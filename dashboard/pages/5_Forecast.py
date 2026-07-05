from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Forecast",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Weather Forecast")

path = Path("outputs/predictions/prophet_forecast.csv")

if not path.exists():
    st.error("Forecast file not found.")
    st.stop()

df = pd.read_csv(path)

st.dataframe(
    df.head(),
    width="stretch",
)

from src.visualization.plots import forecast_plot

fig = forecast_plot(df)

st.plotly_chart(
    fig,
    width="stretch",
)

st.plotly_chart(
    fig,
    width="stretch",
)

st.download_button(
    "Download Forecast",
    df.to_csv(index=False),
    file_name="forecast.csv",
    mime="text/csv",
    width="stretch",
)