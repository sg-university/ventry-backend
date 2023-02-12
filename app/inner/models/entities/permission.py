from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Permission(SQLModel, table=True):
    __tablename__ = "permission"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: Permission):
        self.id = entity.id
        self.name = entity.name
        self.description = entity.description
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
