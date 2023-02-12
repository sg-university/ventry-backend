from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    __tablename__ = "item"
    id: UUID = Field(primary_key=True)
    permission_id: UUID = Field(foreign_key="permission.id")
    code: str
    name: str
    description: str
    combination_max_quantity: float
    combination_min_quantity: float
    quantity: float
    unit_name: str
    unit_sell_price: float
    unit_cost_price: float
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: Item):
        self.id = entity.id
        self.permission_id = entity.permission_id
        self.code = entity.code
        self.name = entity.name
        self.description = entity.description
        self.combination_max_quantity = entity.combination_max_quantity
        self.combination_min_quantity = entity.combination_min_quantity
        self.quantity = entity.quantity
        self.unit_name = entity.unit_name
        self.unit_sell_price = entity.unit_sell_price
        self.unit_cost_price = entity.unit_cost_price
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
