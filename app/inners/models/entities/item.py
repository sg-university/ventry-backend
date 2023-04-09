from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Item(BaseEntity, table=True):
    __tablename__ = "item"
    id: UUID = Field(primary_key=True)
    location_id: UUID = Field(foreign_key="location.id")
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
