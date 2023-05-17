from app.inners.models.value_objects.base_value_object import BaseValueObject


class MetricForecast(BaseValueObject):
    mae: float
    smape: float
