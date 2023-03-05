from pydantic import BaseModel


class ItemStockForecastBody(BaseModel):
    horizon: int
    resample: str
