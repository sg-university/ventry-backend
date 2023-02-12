from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inner.models.entities.base_entity import BaseEntity


class Account(BaseEntity, table=True):
    __tablename__ = "account"
    id: UUID = Field(primary_key=True)
    role_id: UUID = Field(foreign_key="role.id")
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
