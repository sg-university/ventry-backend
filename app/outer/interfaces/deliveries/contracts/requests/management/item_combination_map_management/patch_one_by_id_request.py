from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.patch_body import \
    PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: PatchBody
