from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_item_map_management.transaction_item_map_patch_body import \
    TransactionItemMapPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: TransactionItemMapPatchBody
