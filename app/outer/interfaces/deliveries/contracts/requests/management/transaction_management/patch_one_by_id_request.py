from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_patch_body import \
    TransactionPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: TransactionPatchBody
