from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_file_map_management.item_file_map_patch_body import \
    ItemFileMapPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemFileMapPatchBody
