from app.inners.models.value_objects.base_value_object import BaseValueObject


class LocationRegister(BaseValueObject):
    name: str
    description: str
    address: str
