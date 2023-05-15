from uuid import UUID

from pydantic import BaseModel


class ReadOneByAccountIdRequest(BaseModel):
    account_id: UUID
