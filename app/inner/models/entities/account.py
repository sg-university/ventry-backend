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
