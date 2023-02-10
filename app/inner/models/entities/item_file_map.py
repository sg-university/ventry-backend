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
