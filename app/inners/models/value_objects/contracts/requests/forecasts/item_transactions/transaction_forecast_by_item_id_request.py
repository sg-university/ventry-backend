from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class TransactionForecastByItemIdRequest(BaseValueObject):
    item_id: UUID
    horizon: int
    resample: str
    test_size: float
    eval_metric: str
