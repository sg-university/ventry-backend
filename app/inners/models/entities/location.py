from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Location(BaseEntity, table=True):
    __tablename__ = "location"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
