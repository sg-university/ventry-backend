from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_patch import \
    ItemCombinationMapPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemCombinationMapPatch
