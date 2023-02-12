from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inner.models.entities.base_entity import BaseEntity


class File(BaseEntity, table=True):
    __tablename__ = "file"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    extension: str
    content: bytes
    created_at: datetime
    updated_at: datetime
