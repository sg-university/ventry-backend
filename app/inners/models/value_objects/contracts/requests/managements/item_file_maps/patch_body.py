from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    item_id: UUID
    file_id: UUID