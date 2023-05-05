from uuid import UUID

from pydantic import BaseModel


class StockForecastByItemIdRequest(BaseModel):
    item_id: UUID
    horizon: int
    resample: str
    test_size: float
