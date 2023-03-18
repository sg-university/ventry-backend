from pydantic import BaseModel

from app.inners.models.value_objects.metric_forecast import MetricForecast
from app.inners.models.value_objects.prediction_forecast import PredictionForecast


class ItemTransactionForecastResponse(BaseModel):
    prediction: PredictionForecast
    metric: MetricForecast
