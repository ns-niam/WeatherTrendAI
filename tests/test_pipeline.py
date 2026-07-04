from pathlib import Path

import pandas as pd

from src.data.data_loader import DataLoader
from src.models.predict import Predictor


def test_dataset_exists():

    assert Path(
        "data/raw/weather.csv"
    ).exists()


from config.settings import DATASET_PATH


def test_dataset_load():

    loader = DataLoader(DATASET_PATH)

    df = loader.load()

    assert isinstance(df, pd.DataFrame)

    assert len(df) > 0


def test_model_exists():

    assert Path(
        "outputs/models/best_model.pkl"
    ).exists()


def test_model_prediction():

    predictor = Predictor(
        "outputs/models/best_model.pkl"
    )

    sample = {
        "humidity": 70,
        "pressure_mb": 1013,
        "wind_kph": 12,
        "precip_mm": 0,
        "cloud": 40,
        "visibility_km": 10,
        "uv_index": 5,
        "air_quality_PM2.5": 12,
        "air_quality_PM10": 20,
        "temp_difference": 1,
        "air_quality_score": 15,
        "weather_severity": 3,
        "year": 2026,
        "month": 7,
        "day": 4,
        "hour": 12,
    }

    prediction = predictor.predict_one(sample)

    assert isinstance(
        prediction,
        float,
    )