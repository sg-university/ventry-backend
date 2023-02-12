from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inner.models.entities.base_entity import BaseEntity


class InventoryControl(BaseEntity, table=True):
    __tablename__ = "inventory_control"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    item_id: UUID = Field(foreign_key="item.id")
    quantity_before: float
    quantity_after: float
    timestamp: datetime
    created_at: datetime
    updated_at: datetime
