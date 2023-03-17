from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    role_id: UUID
    name: str
    email: str
    password: str
