from pydantic import BaseModel


class PredictionForecast(BaseModel):
    past: list
    future: list
