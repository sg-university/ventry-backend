from app.inners.models.value_objects.base_value_object import BaseValueObject


class PredictionForecast(BaseValueObject):
    past: list
    future: list
