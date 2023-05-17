from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject


class ReadOneByAccountIdRequest(BaseValueObject):
    account_id: UUID
