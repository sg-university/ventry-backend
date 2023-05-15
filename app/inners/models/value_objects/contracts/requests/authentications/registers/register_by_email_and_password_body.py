from uuid import UUID

from pydantic import BaseModel


class RegisterByEmailAndPasswordBody(BaseModel):
    role_id: UUID
    location_id: UUID
    name: str
    email: str
    password: str
