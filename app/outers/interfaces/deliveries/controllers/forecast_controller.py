from uuid import UUID

from fastapi import APIRouter

from app.inners.use_cases.forecasts import item_stock_forecast, item_transaction_forecast
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

router: APIRouter = APIRouter(prefix="/forecasts", tags=["forecasts"])


@router.post("/items/{item_id}/stock", response_model=Content[ItemStockForecastResponse])
async def item_stock(item_id: UUID, body: StockForecastBody) -> Content[ItemStockForecastResponse]:
    request: StockForecastByItemIdRequest = StockForecastByItemIdRequest(
        item_id=item_id,
        horizon=body.horizon,
        resample=body.resample,
        test_size=body.test_size,
    )
    return await item_stock_forecast.forecast(request)


@router.post("/items/{item_id}/transaction", response_model=Content[ItemTransactionForecastResponse])
async def item_transaction(item_id: UUID, body: TransactionForecastBody) -> Content[
    ItemTransactionForecastResponse]:
    request: TransactionForecastByItemIdRequest = TransactionForecastByItemIdRequest(
        item_id=item_id,
        horizon=body.horizon,
        resample=body.resample,
        test_size=body.test_size,
    )
    return await item_transaction_forecast.forecast(request)
