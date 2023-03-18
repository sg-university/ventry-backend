from pydantic import BaseModel


class StockForecastBody(BaseModel):
    horizon: int
    resample: str
    test_size: int
