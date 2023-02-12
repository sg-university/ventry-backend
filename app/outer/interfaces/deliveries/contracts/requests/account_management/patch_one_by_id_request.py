from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.account_management.account_patch import AccountPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: AccountPatch
