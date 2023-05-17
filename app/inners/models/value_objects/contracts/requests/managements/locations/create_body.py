from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class CreateBody(BaseValueObject):
    company_id: UUID
    name: str
    description: str
    address: str
