from uuid import UUID

from app.inners.models.value_objects.base_value_object import BaseValueObject
from app.inners.models.value_objects.contracts.requests.managements.items.patch_body import PatchBody


class PatchOneByIdRequest(BaseValueObject):
    id: UUID
    body: PatchBody
