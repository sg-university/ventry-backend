from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class ItemBundleMap(BaseEntity, table=True):
    __tablename__ = "item_bundle_map"
    id: UUID = Field(primary_key=True)
    super_item_id: UUID = Field(foreign_key="item.id")
    sub_item_id: UUID = Field(foreign_key="item.id")
    quantity: float
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
