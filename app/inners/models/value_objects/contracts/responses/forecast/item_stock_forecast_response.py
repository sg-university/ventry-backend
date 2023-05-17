from app.inners.models.value_objects.base_value_object import BaseValueObject

from app.inners.models.value_objects.forecasts.metric_forecast import MetricForecast
from app.inners.models.value_objects.forecasts.prediction_forecast import PredictionForecast


class ItemStockForecastResponse(BaseValueObject):
    prediction: PredictionForecast
    metric: MetricForecast
