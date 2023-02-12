from uuid import UUID

from pydantic import BaseModel


class AccountPatch(BaseModel):
    role_id: UUID
    name: str
    email: str
    password: str
