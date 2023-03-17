from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    account_id: UUID
    sell_price: float
    timestamp: datetime
