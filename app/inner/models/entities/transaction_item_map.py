from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class TransactionItemMap(SQLModel, table=True):
    __tablename__ = "transaction_item_map"
    id: UUID = Field(primary_key=True)
    transaction_id: UUID = Field(foreign_key="transaction.id")
    item_id: UUID = Field(foreign_key="item.id")
    sell_price: float
    quantity: float
    created_at: datetime
    updated_at: datetime
