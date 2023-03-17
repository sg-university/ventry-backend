from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    account_id: UUID
    permission_id: UUID
