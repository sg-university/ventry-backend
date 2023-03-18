from pydantic import BaseModel


class TransactionForecastBody(BaseModel):
    horizon: int
    resample: str
    test_size: int
