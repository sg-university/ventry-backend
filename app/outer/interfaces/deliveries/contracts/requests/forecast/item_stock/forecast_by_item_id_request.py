from uuid import UUID

from pydantic import BaseModel


class ForecastByItemIdRequest(BaseModel):
    item_id: UUID
    interval: str
