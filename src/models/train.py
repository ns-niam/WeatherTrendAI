from __future__ import annotations
from config.settings import FEATURES
from config.settings import TARGET
from config.settings import TEST_SIZE
from config.settings import RANDOM_STATE
from pathlib import Path

import joblib
import pandas as pd

from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


class ModelTrainer:


    TARGET_COLUMN = TARGET

    def __init__(
        self,
        dataframe: pd.DataFrame,
        output_dir: str = "outputs/models",
    ):
        self.df = dataframe.copy()
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.models = {
            "Linear Regression": LinearRegression(),
            "Random Forest": RandomForestRegressor(
                n_estimators=50,
                max_depth=15,
                min_samples_split=10,
                min_samples_leaf=5,
                random_state=42,
                n_jobs=-1,
),
            "XGBoost": XGBRegressor(
                n_estimators=200,
                learning_rate=0.05,
                max_depth=6,
                random_state=42,
                n_jobs=-1,
            ),
            "LightGBM": LGBMRegressor(
                random_state=42,
            ),
        }

        self.results = []

        self.best_model = None
        self.best_name = None

    def prepare(self):

        X = self.df[FEATURES]

        y = self.df[TARGET]

        return train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
        )

    def train(self):

        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = self.prepare()

        best_r2 = float("-inf")

        for name, model in self.models.items():

            model.fit(
                X_train,
                y_train,
            )

            prediction = model.predict(
                X_test
            )

            mae = mean_absolute_error(
                y_test,
                prediction,
            )

            rmse = mean_squared_error(
                y_test,
                prediction,
            ) ** 0.5

            r2 = r2_score(
                y_test,
                prediction,
            )

            self.results.append(
                {
                    "Model": name,
                    "MAE": round(mae, 3),
                    "RMSE": round(rmse, 3),
                    "R2": round(r2, 4),
                }
            )

            if r2 > best_r2:

                best_r2 = r2

                self.best_model = model

                self.best_name = name

        return self
    
    def save(self):

        from src.utils.io import save_model

        for name, model in self.models.items():

            filename = (
            name.lower()
            .replace(" ", "_")
            + ".pkl"
        )

        save_model(
            model,
            self.output_dir / filename,
        )

        save_model(
        self.best_model,
        self.output_dir / "best_model.pkl",
    )

        return self.output_dir

    
    def leaderboard(self):

        return (
            pd.DataFrame(self.results)
            .sort_values(
                "R2",
                ascending=False,
            )
            .reset_index(drop=True)
        )

    def summary(self):

        board = self.leaderboard()

        print(board)

        print()

        print(
            f"Best Model: {self.best_name}"
        )

        return board