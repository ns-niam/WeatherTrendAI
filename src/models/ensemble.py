from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
import pandas as pd


class EnsemblePredictor:

    def __init__(self, model_paths: dict[str, str | Path]):

        self.models = {}

        for name, path in model_paths.items():

            self.models[name] = joblib.load(path)

    def predict(
        self,
        dataframe: pd.DataFrame,
        features: list[str],
    ) -> np.ndarray:

        predictions = []

        for model in self.models.values():

            prediction = model.predict(
                dataframe[features]
            )

            predictions.append(prediction)

        predictions = np.array(predictions)

        return predictions.mean(axis=0)

    def predict_one(
        self,
        sample: pd.DataFrame,
        features: list[str],
    ) -> float:

        prediction = self.predict(
            sample,
            features,
        )

        return float(prediction[0])