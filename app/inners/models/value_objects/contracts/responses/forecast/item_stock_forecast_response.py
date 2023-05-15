from pydantic import BaseModel

from app.inners.models.value_objects.forecasts.metric_forecast import MetricForecast
from app.inners.models.value_objects.forecasts.prediction_forecast import PredictionForecast


class ItemStockForecastResponse(BaseModel):
    prediction: PredictionForecast
    metric: MetricForecast
