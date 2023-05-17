from app.inners.models.value_objects.base_value_object import BaseValueObject


class PatchBody(BaseValueObject):
    name: str
    description: str
