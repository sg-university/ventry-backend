from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Transaction(SQLModel, table=True):
    __tablename__ = "transaction"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    sell_price: float
    timestamp: datetime
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: Transaction):
        self.id = entity.id
        self.account_id = entity.account_id
        self.sell_price = entity.sell_price
        self.timestamp = entity.timestamp
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
