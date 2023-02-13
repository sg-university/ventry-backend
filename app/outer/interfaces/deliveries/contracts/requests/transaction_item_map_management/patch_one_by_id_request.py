from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.transaction_item_map_patch import \
    TransactionItemMapPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: TransactionItemMapPatch
