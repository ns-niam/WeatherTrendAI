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

st.caption(
    "Upload a CSV file containing the required weather features to generate batch predictions."
)

predictor = Predictor(
    "outputs/models/best_model.pkl"
)

# Required features
required = predictor.model.feature_names_in_.tolist()

# Download template
template = pd.DataFrame(columns=required)

st.download_button(
    "📥 Download CSV Template",
    template.to_csv(index=False),
    file_name="prediction_template.csv",
    mime="text/csv",
    width="stretch",
)

uploaded = st.file_uploader(
    "Upload CSV",
    type=["csv"],
)

if uploaded:

    df = pd.read_csv(uploaded)

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        width="stretch",
    )

    if st.button(
        " Predict",
        width="stretch",
    ):

        missing = [
            col
            for col in required
            if col not in df.columns
        ]

        if missing:

            st.error(
                "The uploaded CSV is missing required features."
            )

            st.write("### Missing Columns")

            st.write(missing)

            st.info(
                "Please download the template above and upload a CSV with the required columns."
            )

            st.stop()

        try:

            result = predictor.predict(df)

            st.success(
                "Prediction completed successfully."
            )

            st.subheader("Prediction Result")

            st.dataframe(
                result,
                width="stretch",
            )

            st.download_button(
                "⬇ Download Prediction",
                result.to_csv(index=False),
                file_name="weather_predictions.csv",
                mime="text/csv",
                width="stretch",
            )

        except Exception as e:

            st.error(
                f"Prediction failed: {e}"
            )
