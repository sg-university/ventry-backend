from uuid import UUID

from pydantic import BaseModel


class ItemFileMapPatchBody(BaseModel):
    item_id: UUID
    file_id: UUID
