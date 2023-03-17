from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    permission_id: UUID
    code: str
    name: str
    description: str
    combination_max_quantity: float
    combination_min_quantity: float
    quantity: float
    unit_name: str
    unit_sell_price: float
    unit_cost_price: float
