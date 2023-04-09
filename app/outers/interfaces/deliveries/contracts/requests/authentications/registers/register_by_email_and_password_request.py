from uuid import UUID

from pydantic import BaseModel


class RegisterByEmailAndPasswordRequest(BaseModel):
    role_id: UUID
    location_id: UUID
    name: str
    email: str
    password: str
