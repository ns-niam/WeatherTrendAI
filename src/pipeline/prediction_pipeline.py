from __future__ import annotations

from pathlib import Path

import pandas as pd

from config.settings import FEATURES
from src.models.predict import Predictor


class PredictionPipeline:

    def __init__(
        self,
        model_path: str | Path = "outputs/models/best_model.pkl",
    ):
        self.predictor = Predictor(model_path)

    def predict_dataframe(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        return self.predictor.predict(dataframe)

    def predict_csv(
        self,
        input_path: str | Path,
        output_path: str | Path,
    ) -> pd.DataFrame:

        df = pd.read_csv(input_path)

        result = self.predict_dataframe(df)

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        result.to_csv(
            output_path,
            index=False,
        )

        return result

    def predict_sample(
        self,
        sample: dict,
    ) -> float:

        return self.predictor.predict_one(sample)