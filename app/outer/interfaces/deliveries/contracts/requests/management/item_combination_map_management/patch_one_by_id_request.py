from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.item_combination_map_patch_body import \
    ItemCombinationMapPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemCombinationMapPatchBody
