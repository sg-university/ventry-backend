from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    transaction_id: UUID
    item_id: UUID
    sell_price: float
    quantity: float
