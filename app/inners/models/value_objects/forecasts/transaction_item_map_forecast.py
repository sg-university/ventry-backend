from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.value_objects.base_value_object import BaseValueObject


class TransactionItemMapForecast(BaseValueObject):
    transaction_id: UUID = Field(foreign_key="transaction.id")
    item_id: UUID = Field(foreign_key="item.id")
    quantity: float
    timestamp: datetime
