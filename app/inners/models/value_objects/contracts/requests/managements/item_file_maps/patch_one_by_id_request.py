from uuid import UUID

from pydantic import BaseModel

from app.inners.models.value_objects.contracts.requests.managements.item_file_maps.patch_body import \
    PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    body: PatchBody
