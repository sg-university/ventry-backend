from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class File(BaseEntity, table=True):
    __tablename__ = "file"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    extension: str
    content: bytes
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
