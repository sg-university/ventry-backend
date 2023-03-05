import pandas as pd

from app.outer.interfaces.deliveries.contracts.requests.forecast.item_stock.forecast_by_item_id_request import \
    ForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.outer.repositories import inventory_control_repository


async def forecast(request: ForecastByItemIdRequest) -> Content[ItemStockForecastResponse]:
    inventory_controls = await inventory_control_repository.read_all_by_item_id(request.item_id)
    inventory_controls_df = pd.DataFrame([value.__dict__ for value in inventory_controls])

    grouped_inventory_controls_df = inventory_controls_df.sort_values(by=['timestamp'], ascending=True).groupby(
        by=pd.Grouper(key='timestamp', freq='1D')).first()

    cleaned_inventory_controls_df = grouped_inventory_controls_df["timestamp, after_quantity"]
    pass
