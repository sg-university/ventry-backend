from uuid import UUID

from pydantic import BaseModel


class AccountPermissionMapCreateBody(BaseModel):
    account_id: UUID
    permission_id: UUID
