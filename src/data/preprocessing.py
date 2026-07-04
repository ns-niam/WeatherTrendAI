from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataPreprocessor:
    """Preprocessing utilities."""

    FEATURE_COLUMNS = [
        "humidity",
        "pressure_mb",
        "wind_kph",
        "precip_mm",
        "cloud",
        "visibility_km",
        "uv_index",
        "air_quality_PM2.5",
        "air_quality_PM10",
    ]

    TARGET_COLUMN = "temperature_celsius"

    REQUIRED_COLUMNS = FEATURE_COLUMNS + [
        TARGET_COLUMN,
        "last_updated",
    ]

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()
        self.scaler = StandardScaler()

    def clean(self) -> "DataPreprocessor":
        self.df = (
            self.df
            .drop_duplicates()
            .dropna()
            .reset_index(drop=True)
        )
        return self

    def validate(self) -> "DataPreprocessor":
        missing = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in self.df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        return self

    def add_datetime_features(self) -> "DataPreprocessor":
        self.df["last_updated"] = pd.to_datetime(
            self.df["last_updated"]
        )

        self.df["year"] = self.df["last_updated"].dt.year
        self.df["month"] = self.df["last_updated"].dt.month
        self.df["day"] = self.df["last_updated"].dt.day
        self.df["hour"] = self.df["last_updated"].dt.hour

        return self

    def scale(
        self,
        columns: list[str] | None = None,
    ) -> "DataPreprocessor":

        columns = columns or self.FEATURE_COLUMNS

        self.df[columns] = self.scaler.fit_transform(
            self.df[columns]
        )

        return self

    def dataframe(self) -> pd.DataFrame:
        return self.df