from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from config.settings import FEATURES


class Predictor:

    def __init__(self, model_path: str | Path):
        self.model_path = Path(model_path)

        if not self.model_path.exists():
            raise FileNotFoundError(self.model_path)

        self.model = joblib.load(self.model_path)

    def predict(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        missing = [
            column
            for column in FEATURES
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing features: {missing}"
            )

        result = dataframe.copy()

        result["prediction"] = self.model.predict(
            result[FEATURES]
        )

        return result

    def predict_csv(
        self,
        input_path: str,
        output_path: str,
    ) -> pd.DataFrame:

        from src.utils.io import load_csv

        df = load_csv(input_path)

        result = self.predict(df)

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        result.to_csv(
            output_path,
            index=False,
        )

        return result

    def predict_one(
        self,
        sample: dict,
    ) -> float:

        df = pd.DataFrame([sample])

        prediction = self.model.predict(
            df[FEATURES]
        )

        return float(prediction[0])