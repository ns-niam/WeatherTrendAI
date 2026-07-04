from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = ROOT_DIR / "outputs"
MODEL_DIR = OUTPUT_DIR / "models"
RESULT_DIR = OUTPUT_DIR / "results"
REPORT_DIR = OUTPUT_DIR / "reports"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

DATASET_NAME = "weather.csv"
DATASET_PATH = RAW_DATA_DIR / DATASET_NAME

TARGET = "temperature_celsius"

RAW_FEATURES = [
    "humidity",
    "pressure_mb",
    "wind_kph",
    "precip_mm",
    "cloud",
    "visibility_km",
    "uv_index",
    "air_quality_PM2.5",
    "air_quality_PM10",
]

ENGINEERED_FEATURES = [
    "temp_difference",
    "air_quality_score",
    "weather_severity",
    "year",
    "month",
    "day",
    "hour",
]

FEATURES = RAW_FEATURES + ENGINEERED_FEATURES

REQUIRED_COLUMNS = RAW_FEATURES + [
    TARGET,
    "last_updated",
    "feels_like_celsius",
]

TEST_SIZE = 0.2
RANDOM_STATE = 42