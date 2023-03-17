from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    account_id: UUID
    sell_price: float
    timestamp: datetime
