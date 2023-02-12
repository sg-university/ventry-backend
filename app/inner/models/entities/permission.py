from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inner.models.entities.base_entity import BaseEntity


class Permission(BaseEntity, table=True):
    __tablename__ = "permission"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
