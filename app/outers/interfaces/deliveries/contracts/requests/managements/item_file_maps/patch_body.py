from uuid import UUID

from pydantic import BaseModel


class PatchBody(BaseModel):
    item_id: UUID
    file_id: UUID
