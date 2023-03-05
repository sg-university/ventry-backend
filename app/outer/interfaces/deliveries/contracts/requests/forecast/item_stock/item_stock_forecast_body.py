from pydantic import BaseModel


class ItemStockForecastData(BaseModel):
    interval: str
