from datetime import datetime
from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class CreateBody(BaseValueObject):
    account_id: UUID
    item_id: UUID
    quantity_before: float
    quantity_after: float
    timestamp: datetime
