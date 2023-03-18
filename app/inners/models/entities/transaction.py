from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class Transaction(BaseEntity, table=True):
    __tablename__ = "transaction"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    sell_price: float
    timestamp: datetime
    created_at: datetime
    updated_at: datetime
