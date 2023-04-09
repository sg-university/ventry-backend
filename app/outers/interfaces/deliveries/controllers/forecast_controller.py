from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.use_cases.forecasts.item_stock_forecast import ItemStockForecast
from app.inners.use_cases.forecasts.item_transaction_forecast import ItemTransactionForecast
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_stocks.stock_forecast_body import \
    StockForecastBody
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_stocks.stock_forecast_by_item_id_request import \
    StockForecastByItemIdRequest
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_transactions.transaction_forecast_body import \
    TransactionForecastBody
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_transactions.transaction_forecast_by_item_id_request import \
    TransactionForecastByItemIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.interfaces.deliveries.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.outers.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse

router: APIRouter = APIRouter(tags=["forecasts"])


@cbv(router)
class ForecastController:
    def __init__(self):
        self.item_stock_forecast: ItemStockForecast = ItemStockForecast()
        self.item_transaction_forecast: ItemTransactionForecast = ItemTransactionForecast()

    @router.post("/forecasts/items/{item_id}/stock")
    async def item_stock(self, item_id: UUID, body: StockForecastBody) -> Content[ItemStockForecastResponse]:
        request: StockForecastByItemIdRequest = StockForecastByItemIdRequest(
            item_id=item_id,
            horizon=body.horizon,
            resample=body.resample,
            test_size=body.test_size,
        )
        return await self.item_stock_forecast.forecast(request)

    @router.post("/forecasts/items/{item_id}/transaction")
    async def item_transaction(self, item_id: UUID, body: TransactionForecastBody) -> Content[
        ItemTransactionForecastResponse]:
        request: TransactionForecastByItemIdRequest = TransactionForecastByItemIdRequest(
            item_id=item_id,
            horizon=body.horizon,
            resample=body.resample,
            test_size=body.test_size,
        )
        return await self.item_transaction_forecast.forecast(request)
