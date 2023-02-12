from uuid import UUID

from pydantic import BaseModel


class ItemFileMapPatch(BaseModel):
    item_id: UUID
    file_id: UUID
