from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class TransactionItemMap(BaseEntity, table=True):
    __tablename__ = "transaction_item_map"
    id: UUID = Field(primary_key=True)
    transaction_id: UUID = Field(foreign_key="transaction.id")
    item_id: UUID = Field(foreign_key="item.id")
    sell_price: float
    quantity: float
    created_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
    updated_at: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True)))
