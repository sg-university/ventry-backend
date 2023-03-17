from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    account_id: UUID
    permission_id: UUID
