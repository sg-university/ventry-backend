from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    company_id: UUID
    name: str
    description: str
    address: str
