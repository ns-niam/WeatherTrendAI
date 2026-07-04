from pydantic import BaseModel


class PredictionRequest(BaseModel):
    humidity: float
    pressure_mb: float
    wind_kph: float
    precip_mm: float
    cloud: float
    visibility_km: float
    uv_index: float
    air_quality_PM2_5: float
    air_quality_PM10: float
    temp_difference: float
    air_quality_score: float
    weather_severity: float
    year: int
    month: int
    day: int
    hour: int


class PredictionResponse(BaseModel):
    temperature: float
    model: str