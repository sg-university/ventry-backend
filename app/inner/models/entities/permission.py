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
