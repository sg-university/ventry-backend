from app.inners.models.value_objects.base_value_object import BaseValueObject


class AccountRegister(BaseValueObject):
    name: str
    email: str
    password: str
