from __future__ import annotations

from config.settings import DATASET_PATH

from src.data.data_loader import DataLoader
from src.data.preprocessing import DataPreprocessor
from src.features.feature_engineering import FeatureEngineer
from src.models.train import ModelTrainer
from src.models.evaluate import ModelEvaluator


class TrainingPipeline:

    def run(self):

        loader = DataLoader(DATASET_PATH)

        df = loader.load()

        df = (
            DataPreprocessor(df)
            .validate()
            .clean()
            .add_datetime_features()
            .dataframe()
        )

        df = (
            FeatureEngineer(df)
            .build()
        )

        trainer = ModelTrainer(df)

        trainer.train()

        leaderboard = trainer.summary()

        trainer.save()

        (
            ModelEvaluator(leaderboard)
            .save()
            .plot()
        )

        return leaderboard