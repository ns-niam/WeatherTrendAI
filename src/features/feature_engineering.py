from __future__ import annotations

import numpy as np
import pandas as pd


class FeatureEngineer:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def add_temperature_features(self):
        if {
            "temperature_celsius",
            "feels_like_celsius",
        }.issubset(self.df.columns):

            self.df["temp_difference"] = (
                self.df["feels_like_celsius"]
                - self.df["temperature_celsius"]
            )

        return self

    def add_wind_features(self):
        if "wind_kph" in self.df.columns:

            self.df["wind_category"] = pd.cut(
                self.df["wind_kph"],
                bins=[-1, 5, 20, 40, np.inf],
                labels=[
                    "Calm",
                    "Light",
                    "Moderate",
                    "Strong",
                ],
            )

        return self

    def add_humidity_features(self):
        if "humidity" in self.df.columns:

            self.df["humidity_level"] = pd.cut(
                self.df["humidity"],
                bins=[0, 30, 60, 100],
                labels=[
                    "Low",
                    "Normal",
                    "High",
                ],
            )

        return self

    def add_pressure_features(self):
        if "pressure_mb" in self.df.columns:

            self.df["pressure_level"] = pd.cut(
                self.df["pressure_mb"],
                bins=[900, 1005, 1018, 1100],
                labels=[
                    "Low",
                    "Normal",
                    "High",
                ],
            )

        return self

    def add_air_quality_score(self):

        columns = [
            "air_quality_PM2.5",
            "air_quality_PM10",
            "air_quality_Ozone",
            "air_quality_Carbon_Monoxide",
        ]

        available = [
            c for c in columns
            if c in self.df.columns
        ]

        if available:

            self.df["air_quality_score"] = (
                self.df[available]
                .mean(axis=1)
            )

        return self

    def add_day_night(self):

        if "hour" in self.df.columns:

            self.df["is_day"] = (
                (self.df["hour"] >= 6)
                &
                (self.df["hour"] < 18)
            ).astype(int)

        return self

    def add_weather_severity(self):

        required = {
            "wind_kph",
            "precip_mm",
            "cloud",
        }

        if required.issubset(self.df.columns):

            self.df["weather_severity"] = (
                self.df["wind_kph"] * 0.3
                + self.df["precip_mm"] * 2
                + self.df["cloud"] * 0.2
            )

        return self

    def build(self):

        return (
            self
            .add_temperature_features()
            .add_wind_features()
            .add_humidity_features()
            .add_pressure_features()
            .add_air_quality_score()
            .add_day_night()
            .add_weather_severity()
            .df
        )