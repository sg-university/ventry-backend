from uuid import UUID

from pydantic import BaseModel


class CreateBody(BaseModel):
    item_id: UUID
    file_id: UUID
