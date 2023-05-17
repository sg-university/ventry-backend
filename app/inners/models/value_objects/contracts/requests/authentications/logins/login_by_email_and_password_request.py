from app.inners.models.value_objects.base_value_object import BaseValueObject


class LoginByEmailAndPasswordRequest(BaseValueObject):
    email: str
    password: str
