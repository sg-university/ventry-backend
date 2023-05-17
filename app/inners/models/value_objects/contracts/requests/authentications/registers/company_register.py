from app.inners.models.value_objects.base_value_object import BaseValueObject


class CompanyRegister(BaseValueObject):
    name: str
    description: str
    address: str
