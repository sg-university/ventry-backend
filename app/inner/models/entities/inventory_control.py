from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class InventoryControl(SQLModel, table=True):
    __tablename__ = "inventory_control"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    item_id: UUID = Field(foreign_key="item.id")
    quantity_before: float
    quantity_after: float
    timestamp: datetime
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: InventoryControl):
        self.id = entity.id
        self.account_id = entity.account_id
        self.item_id = entity.item_id
        self.quantity_before = entity.quantity_before
        self.quantity_after = entity.quantity_after
        self.timestamp = entity.timestamp
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
