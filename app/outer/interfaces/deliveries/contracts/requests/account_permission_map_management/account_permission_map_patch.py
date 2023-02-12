from uuid import UUID

from pydantic import BaseModel


class AccountPermissionMapPatch(BaseModel):
    account_id: UUID
    permission_id: UUID
