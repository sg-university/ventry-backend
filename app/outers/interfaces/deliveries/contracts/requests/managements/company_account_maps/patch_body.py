from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    company_id: UUID
    account_id: UUID
