from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_item_map_management.patch_body import \
    PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: PatchBody
