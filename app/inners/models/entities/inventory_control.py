from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class InventoryControl(BaseEntity, table=True):
    __tablename__ = "inventory_control"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    item_id: UUID = Field(foreign_key="item.id")
    quantity_before: float
    quantity_after: float
    timestamp: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
