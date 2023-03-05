from uuid import UUID

from pydantic import BaseModel


class TransactionItemMapPatchBody(BaseModel):
    transaction_id: UUID
    item_id: UUID
    sell_price: float
    quantity: float
