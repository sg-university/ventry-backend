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
