from uuid import UUID

from pydantic import BaseModel


class AccountCreate(BaseModel):
    role_id: UUID
    name: str
    email: str
    password: str
