from pydantic import BaseModel


class MetricForecast(BaseModel):
    mae: float
    smape: float
