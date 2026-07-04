from pathlib import Path

from src.models.predict import Predictor


MODEL_PATH = Path("outputs/models/best_model.pkl")

predictor = Predictor(MODEL_PATH)