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