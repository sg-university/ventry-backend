from uuid import UUID

from pydantic import BaseModel


class AccountPermissionMapCreate(BaseModel):
    account_id: UUID
    permission_id: UUID
