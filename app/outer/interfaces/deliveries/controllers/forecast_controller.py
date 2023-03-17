from uuid import UUID

from fastapi import APIRouter

from app.inner.use_cases.forecast import item_stock_forecast, item_transaction_forecast
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_stock.item_stock_forecast_body import \
    ItemStockForecastBody
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_stock.stock_forecast_by_item_id_request import \
    StockForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_transaction.item_transaction_forecast_body import \
    ItemTransactionForecastBody
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_transaction.transaction_forecast_by_item_id_request import \
    TransactionForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.responses.content import Content
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse

router: APIRouter = APIRouter(prefix="/forecasts", tags=["forecasts"])


@router.post("/items/{item_id}/stock", response_model=Content[ItemStockForecastResponse])
async def item_stock(item_id: UUID, entity: ItemStockForecastBody) -> Content[ItemStockForecastResponse]:
    request: StockForecastByItemIdRequest = StockForecastByItemIdRequest(
        item_id=item_id,
        horizon=entity.horizon,
        resample=entity.resample,
    )
    return await item_stock_forecast.forecast(request)


@router.post("/items/{item_id}/transaction", response_model=Content[ItemTransactionForecastResponse])
async def item_transaction(item_id: UUID, entity: ItemTransactionForecastBody) -> Content[
    ItemTransactionForecastResponse]:
    request: TransactionForecastByItemIdRequest = TransactionForecastByItemIdRequest(
        item_id=item_id,
        horizon=entity.horizon,
        resample=entity.resample,
    )
    return await item_transaction_forecast.forecast(request)
