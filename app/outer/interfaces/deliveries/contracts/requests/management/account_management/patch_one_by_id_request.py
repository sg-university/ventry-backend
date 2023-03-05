from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.account_management.account_patch_body import \
    AccountPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: AccountPatchBody
