from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class InventoryControlCreate(BaseModel):
    account_id: UUID
    item_id: UUID
    quantity_before: float
    quantity_after: float
    timestamp: datetime
