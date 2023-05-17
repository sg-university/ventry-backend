from app.inners.models.value_objects.base_value_object import BaseValueObject

from app.inners.models.value_objects.contracts.requests.managements.items.create_body import \
    CreateBody


class CreateOneRequest(BaseValueObject):
    body: CreateBody
