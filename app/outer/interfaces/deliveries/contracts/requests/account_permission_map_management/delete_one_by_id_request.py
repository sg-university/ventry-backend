from uuid import UUID

from pydantic import BaseModel


class DeleteOneByIdRequest(BaseModel):
    id: UUID
