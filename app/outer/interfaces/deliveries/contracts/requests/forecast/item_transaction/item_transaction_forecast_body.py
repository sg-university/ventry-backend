from pydantic import BaseModel


class ItemStockForecastBody(BaseModel):
    interval: str
