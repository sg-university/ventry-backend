from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class ItemFileMap(BaseEntity, table=True):
    __tablename__ = "item_file_map"
    id: UUID = Field(primary_key=True)
    item_id: UUID = Field(foreign_key="item.id")
    file_id: UUID = Field(foreign_key="file.id")
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
