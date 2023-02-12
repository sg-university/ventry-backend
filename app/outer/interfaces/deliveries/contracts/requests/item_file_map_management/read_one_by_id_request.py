from uuid import UUID

from pydantic import BaseModel


class ReadOneByIdRequest(BaseModel):
    id: UUID
