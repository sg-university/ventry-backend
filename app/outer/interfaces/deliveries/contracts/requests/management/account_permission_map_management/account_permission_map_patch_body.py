from uuid import UUID

from pydantic import BaseModel


class AccountPermissionMapPatchBody(BaseModel):
    account_id: UUID
    permission_id: UUID
