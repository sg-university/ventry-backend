from typing import Optional
from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    location_id: UUID
    code: str
    name: str
    type: str
    description: str
    quantity: float
    unit_name: str
    unit_sell_price: float
    unit_cost_price: float
    image: Optional[bytes]
