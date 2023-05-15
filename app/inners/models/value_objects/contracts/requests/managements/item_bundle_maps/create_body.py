from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    super_item_id: UUID
    sub_item_id: UUID
    quantity: float
