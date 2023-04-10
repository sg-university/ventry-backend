from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Company(BaseEntity, table=True):
    __tablename__ = "company"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    address: str
    created_at: datetime
    updated_at: datetime
