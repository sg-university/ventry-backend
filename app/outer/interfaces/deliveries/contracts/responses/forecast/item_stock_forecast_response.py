from pydantic import BaseModel

from app.inner.models.value_objects.metric_forecast import MetricForecast
from app.inner.models.value_objects.prediction_forecast import PredictionForecast


class ItemStockForecastResponse(BaseModel):
    prediction: PredictionForecast
    metric: MetricForecast
