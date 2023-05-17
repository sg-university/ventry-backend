from app.inners.models.value_objects.base_value_object import BaseValueObject


class CreateBody(BaseValueObject):
    name: str
    description: str
    extension: str
    content: bytes
