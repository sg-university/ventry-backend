from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class TransactionPatch(BaseModel):
    account_id: UUID
    sell_price: float
    timestamp: datetime
