from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Account(BaseEntity, table=True):
    __tablename__ = "account"
    id: UUID = Field(primary_key=True)
    role_id: UUID = Field(foreign_key="role.id")
    location_id: UUID = Field(foreign_key="location.id")
    name: str
    email: str
    password: str
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
