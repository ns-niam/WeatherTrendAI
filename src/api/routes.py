from fastapi import APIRouter

from src.api.schemas import (
    PredictionRequest,
    PredictionResponse,
)

from src.api.service import PredictionService


router = APIRouter()


@router.get("/")
def home():

    return {
        "project": "WeatherTrendAI",
        "status": "running",
    }


@router.get("/health")
def health():

    return {
        "status": "healthy",
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(
    request: PredictionRequest,
):

    return PredictionService.predict(
        request.model_dump()
    )