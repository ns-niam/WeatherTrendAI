from __future__ import annotations

import pandas as pd

from src.api.dependencies import predictor


class PredictionService:

    @staticmethod
    def predict(data: dict) -> dict:

        df = pd.DataFrame([{
            "humidity": data["humidity"],
            "pressure_mb": data["pressure_mb"],
            "wind_kph": data["wind_kph"],
            "precip_mm": data["precip_mm"],
            "cloud": data["cloud"],
            "visibility_km": data["visibility_km"],
            "uv_index": data["uv_index"],
            "air_quality_PM2.5": data["air_quality_PM2_5"],
            "air_quality_PM10": data["air_quality_PM10"],
            "temp_difference": data["temp_difference"],
            "air_quality_score": data["air_quality_score"],
            "weather_severity": data["weather_severity"],
            "year": data["year"],
            "month": data["month"],
            "day": data["day"],
            "hour": data["hour"],
        }])

        prediction = predictor.predict(df)
        temperature = prediction["prediction"].iloc[0]

        return {
        "temperature": float(temperature),
        "model": "Random Forest",
        }