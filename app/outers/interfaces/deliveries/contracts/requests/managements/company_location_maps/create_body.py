from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    company_id: UUID
    location_id: UUID