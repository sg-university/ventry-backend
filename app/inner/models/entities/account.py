from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Account(SQLModel, table=True):
    __tablename__ = "account"
    id: UUID = Field(primary_key=True)
    role_id: UUID = Field(foreign_key="role.id")
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: Account):
        self.id = entity.id
        self.role_id = entity.role_id
        self.name = entity.name
        self.email = entity.email
        self.password = entity.password
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
