from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class File(SQLModel, table=True):
    __tablename__ = "file"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    extension: str
    content: bytes
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: File):
        self.id = entity.id
        self.name = entity.name
        self.description = entity.description
        self.extension = entity.extension
        self.content = entity.content
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
