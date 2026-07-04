from pathlib import Path
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.predict import Predictor


st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide",
)

st.title("📂 Batch Prediction")

predictor = Predictor("outputs/models/best_model.pkl")

uploaded = st.file_uploader(
    "Upload CSV",
    type=["csv"],
)

if uploaded:

    df = pd.read_csv(uploaded)

    st.dataframe(
        df.head(),
        width="stretch",
    )

    if st.button("Predict", width="stretch"):

        result = predictor.predict(df)

        st.dataframe(
            result,
            width="stretch",
        )

        st.download_button(
            "Download CSV",
            result.to_csv(index=False),
            file_name="prediction.csv",
            mime="text/csv",
            width="stretch",
        )