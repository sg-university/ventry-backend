from pydantic import BaseModel


class ItemTransactionForecastBody(BaseModel):
    horizon: int
    resample: str
