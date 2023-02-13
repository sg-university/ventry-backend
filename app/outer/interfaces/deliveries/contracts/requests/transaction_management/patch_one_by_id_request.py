from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_patch import TransactionPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: TransactionPatch
