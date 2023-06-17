from datetime import datetime
from typing import Optional
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Item(BaseEntity, table=True):
    __tablename__ = "item"
    id: UUID = Field(primary_key=True)
    location_id: UUID = Field(foreign_key="location.id")
    code: str
    name: str
    type: str
    description: str
    quantity: float
    unit_name: str
    unit_sell_price: float
    unit_cost_price: float
    image: Optional[bytes]
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
