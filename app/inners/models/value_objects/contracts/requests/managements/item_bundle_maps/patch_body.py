from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    super_item_id: UUID
    sub_item_id: UUID
    quantity: float
