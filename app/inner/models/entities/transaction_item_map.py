from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inner.models.entities.base_entity import BaseEntity


class TransactionItemMap(BaseEntity, table=True):
    __tablename__ = "transaction_item_map"
    id: UUID = Field(primary_key=True)
    transaction_id: UUID = Field(foreign_key="transaction.id")
    item_id: UUID = Field(foreign_key="item.id")
    sell_price: float
    quantity: float
    created_at: datetime
    updated_at: datetime
