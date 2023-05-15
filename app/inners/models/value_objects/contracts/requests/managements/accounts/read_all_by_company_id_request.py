from uuid import UUID

from pydantic import BaseModel


class ReadAllByCompanyIdRequest(BaseModel):
    company_id: UUID
