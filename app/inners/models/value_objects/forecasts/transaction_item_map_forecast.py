from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class TransactionItemMapForecast(BaseEntity):
    transaction_id: UUID = Field(foreign_key="transaction.id")
    item_id: UUID = Field(foreign_key="item.id")
    quantity: float
    timestamp: datetime
