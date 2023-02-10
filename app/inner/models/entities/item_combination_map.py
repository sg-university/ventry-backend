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
