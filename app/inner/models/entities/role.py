from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    __tablename__ = "role"
    id: UUID = Field(primary_key=True)
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
