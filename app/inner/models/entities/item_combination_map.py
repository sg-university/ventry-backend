from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class ItemCombinationMap(SQLModel, table=True):
    __tablename__ = "item_combination_map"
    id: UUID = Field(primary_key=True)
    super_item_id: UUID = Field(foreign_key="item.id")
    sub_item_id: UUID = Field(foreign_key="item.id")
    quantity: float
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: ItemCombinationMap):
        self.id = entity.id
        self.super_item_id = entity.super_item_id
        self.sub_item_id = entity.sub_item_id
        self.quantity = entity.quantity
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
