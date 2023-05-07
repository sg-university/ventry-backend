from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Location(BaseEntity, table=True):
    __tablename__ = "location"
    id: UUID = Field(primary_key=True)
    company_id: UUID = Field(foreign_key="company.id")
    name: str
    description: str
    address: str
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
