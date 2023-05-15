from uuid import UUID

from pydantic import BaseModel

from app.inners.models.value_objects.contracts.requests.managements.inventory_controls.patch_body import \
    PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    body: PatchBody
