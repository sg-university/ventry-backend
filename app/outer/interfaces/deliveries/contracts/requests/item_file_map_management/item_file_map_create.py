from uuid import UUID

from pydantic import BaseModel


class ItemFileMapCreate(BaseModel):
    item_id: UUID
    file_id: UUID
