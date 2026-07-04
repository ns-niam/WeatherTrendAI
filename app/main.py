from src.data.data_loader import DataLoader
from src.data.preprocessing import DataPreprocessor
from src.features.feature_engineering import FeatureEngineer

loader = DataLoader("data/raw/Global Weather Repository.csv")

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

print(df.head())

from src.models.train import ModelTrainer

trainer = ModelTrainer(df)

trainer.train()

trainer.summary()

trainer.save()


from src.models.evaluate import ModelEvaluator

leaderboard = trainer.summary()

(
    ModelEvaluator(leaderboard)
    .save()
    .plot()
)


from src.models.predict import Predictor

predictor = Predictor(
    "outputs/models/best_model.pkl"
)

predictions = predictor.predict(df)

print(
    predictions[
        [
            "location_name",
            "temperature_celsius",
            "prediction",
        ]
    ].head()
)