from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import StandardScaler

from config.settings import FEATURES
from config.settings import TARGET


class DataPreprocessor:
    """Preprocessing utilities."""

    REQUIRED_COLUMNS = FEATURES + [
        TARGET,
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

        columns = columns or FEATURES

        self.df[columns] = self.scaler.fit_transform(
            self.df[columns]
        )

        return self

    def dataframe(self) -> pd.DataFrame:
        return self.df