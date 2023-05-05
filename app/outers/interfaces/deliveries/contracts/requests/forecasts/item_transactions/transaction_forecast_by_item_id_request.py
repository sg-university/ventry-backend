from uuid import UUID

from pydantic import BaseModel


class TransactionForecastByItemIdRequest(BaseModel):
    item_id: UUID
    horizon: int
    resample: str
    test_size: float
