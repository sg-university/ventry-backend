from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class ItemFileMap(SQLModel, table=True):
    __tablename__ = "item_file_map"
    id: UUID = Field(primary_key=True)
    item_id: UUID = Field(foreign_key="item.id")
    file_id: UUID = Field(foreign_key="file.id")
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: ItemFileMap):
        self.id = entity.id
        self.item_id = entity.item_id
        self.file_id = entity.file_id
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
