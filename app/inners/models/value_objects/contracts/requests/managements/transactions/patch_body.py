from datetime import datetime
from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    account_id: UUID
    sell_price: float
    timestamp: datetime
