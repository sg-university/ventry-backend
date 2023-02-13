from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_patch import \
    ItemFileMapPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemFileMapPatch
