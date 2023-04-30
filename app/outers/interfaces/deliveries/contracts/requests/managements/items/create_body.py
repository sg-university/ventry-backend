from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    location_id: UUID
    code: str
    name: str
    description: str
    quantity: float
    unit_name: str
    unit_sell_price: float
    unit_cost_price: float
