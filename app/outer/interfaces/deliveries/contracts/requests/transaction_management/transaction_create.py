from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    account_id: UUID
    sell_price: float
    timestamp: datetime
