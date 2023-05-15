from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    company_id: UUID
    name: str
    description: str
    address: str
