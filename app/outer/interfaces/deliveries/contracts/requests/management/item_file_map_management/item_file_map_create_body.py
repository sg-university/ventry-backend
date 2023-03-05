from uuid import UUID

from pydantic import BaseModel


class ItemFileMapCreateBody(BaseModel):
    item_id: UUID
    file_id: UUID
