from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class CreateBody(BaseValueObject):
    role_id: UUID
    location_id: UUID
    name: str
    email: str
    password: str
