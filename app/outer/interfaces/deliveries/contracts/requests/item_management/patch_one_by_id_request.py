from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_management.item_patch import ItemPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemPatch
