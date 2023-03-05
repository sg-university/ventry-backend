from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_management.item_patch_body import ItemPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: ItemPatchBody
