from app.inner.models.entities.inventory_control import InventoryControl
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_stock.forecast_by_item_id_request import \
    ForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse
from app.outer.repositories import inventory_control_repository


async def forecast(request: ForecastByItemIdRequest) -> Content[ItemTransactionForecastResponse]:
    inventory_control_histories: [InventoryControl] = await inventory_control_repository.read_all()
