from __future__ import annotations

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

    def patch_from(self, entity: TransactionItemMap):
        self.id = entity.id
        self.transaction_id = entity.transaction_id
        self.item_id = entity.item_id
        self.sell_price = entity.sell_price
        self.quantity = entity.quantity
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
