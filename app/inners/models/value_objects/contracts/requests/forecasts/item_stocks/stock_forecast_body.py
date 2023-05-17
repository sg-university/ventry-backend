from app.inners.models.value_objects.base_value_object import BaseValueObject


class StockForecastBody(BaseValueObject):
    horizon: int
    resample: str
    test_size: float
