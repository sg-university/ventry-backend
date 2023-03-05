from pydantic import BaseModel


class MetricForecast(BaseModel):
    mae: float
    mape: float
