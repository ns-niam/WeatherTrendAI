from pathlib import Path
import sys
from datetime import datetime

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.models.predict import Predictor


st.set_page_config(
    page_title="Single Prediction",
    page_icon="🌡️",
    layout="wide",
)


@st.cache_resource
def load_model():
    return Predictor("outputs/models/best_model.pkl")


predictor = load_model()


st.title("🌡️ Single Weather Prediction")
st.caption("Predict temperature using the trained Random Forest model.")

with st.form("prediction_form"):

    left, right = st.columns(2)

    with left:

        humidity = st.slider("Humidity (%)", 0, 100, 70)

        pressure = st.number_input(
            "Pressure (mb)",
            value=1013.0,
        )

        wind = st.number_input(
            "Wind Speed (kph)",
            value=10.0,
        )

        precip = st.number_input(
            "Precipitation (mm)",
            value=0.0,
        )

        cloud = st.slider(
            "Cloud (%)",
            0,
            100,
            40,
        )

        visibility = st.number_input(
            "Visibility (km)",
            value=10.0,
        )

        uv = st.slider(
            "UV Index",
            0,
            12,
            5,
        )

    with right:

        pm25 = st.number_input(
            "PM2.5",
            value=12.0,
        )

        pm10 = st.number_input(
            "PM10",
            value=20.0,
        )

        feels_like = st.number_input(
            "Feels Like Temperature",
            value=25.0,
        )

        actual_temp = st.number_input(
            "Current Temperature",
            value=24.0,
        )

        air_quality = st.number_input(
            "Air Quality Score",
            value=15.0,
        )

        severity = st.slider(
            "Weather Severity",
            0,
            10,
            3,
        )

    predict_btn = st.form_submit_button(
        "🚀 Predict Temperature",
        width="stretch",
    )

if predict_btn:

    now = datetime.now()

    sample = {
        "humidity": humidity,
        "pressure_mb": pressure,
        "wind_kph": wind,
        "precip_mm": precip,
        "cloud": cloud,
        "visibility_km": visibility,
        "uv_index": uv,
        "air_quality_PM2.5": pm25,
        "air_quality_PM10": pm10,
        "temp_difference": feels_like - actual_temp,
        "air_quality_score": air_quality,
        "weather_severity": severity,
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
    }

    with st.spinner("Predicting..."):

        prediction = predictor.predict_one(sample)

    st.success("Prediction completed successfully.")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🌡️ Temperature",
        f"{prediction:.2f} °C",
    )

    c2.metric(
        "🤖 Model",
        "Random Forest",
    )

    c3.metric(
        "⏰ Time",
        now.strftime("%H:%M"),
    )

    if prediction < 10:
        status = "❄️ Cold"
    elif prediction < 25:
        status = "🌤️ Pleasant"
    elif prediction < 35:
        status = "☀️ Warm"
    else:
        status = "🔥 Hot"

    st.info(f"Weather Status: {status}")

    with st.expander("Input Summary"):

        st.dataframe(
            pd.DataFrame([sample]),
            width="stretch",
            hide_index=True,
        )