import json

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.entities.item import Item
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.inners.models.entities.transaction import Transaction
from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_stocks.stock_forecast_body import \
    StockForecastBody
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_transactions.transaction_forecast_body import \
    TransactionForecastBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.inventory_control_repository import InventoryControlRepository
from app.outers.repositories.item_repository import ItemRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from app.outers.repositories.transaction_item_map_repository import TransactionItemMapRepository
from app.outers.repositories.transaction_repository import TransactionRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.inventory_control_mock_data import inventory_control_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.mock_data.transaction_item_map_mock_data import transaction_item_map_mock_data
from test.mock_data.transaction_mock_data import transaction_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
location_repository: LocationRepository = LocationRepository()
account_repository: AccountRepository = AccountRepository()
item_repository: ItemRepository = ItemRepository()
inventory_control_repository: InventoryControlRepository = InventoryControlRepository()
transaction_repository: TransactionRepository = TransactionRepository()
transaction_item_map_repository: TransactionItemMapRepository = TransactionItemMapRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for location in location_mock_data:
        await location_repository.create_one(Location(**location.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))

    for item in item_mock_data:
        await item_repository.create_one(Item(**item.dict()))

    for inventory_control in inventory_control_mock_data:
        await inventory_control_repository.create_one(InventoryControl(**inventory_control.dict()))

    for transaction in transaction_mock_data:
        await transaction_repository.create_one(Transaction(**transaction.dict()))

    for transaction_item_map in transaction_item_map_mock_data:
        await transaction_item_map_repository.create_one(TransactionItemMap(**transaction_item_map.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for transaction_item_map in transaction_item_map_mock_data:
        await transaction_item_map_repository.delete_one_by_id(transaction_item_map.id)

    for inventory_control in inventory_control_mock_data:
        await inventory_control_repository.delete_one_by_id(inventory_control.id)

    for item in item_mock_data:
        await item_repository.delete_one_by_id(item.id)

    for account in account_mock_data:
        await account_repository.delete_one_by_id(account.id)

    for location in location_mock_data:
        await location_repository.delete_one_by_id(location.id)

    for role in role_mock_data:
        await role_repository.delete_one_by_id(role.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__forecast_item_stock__should_get_forecast_item_stock__success():
    item_stock_forecast: StockForecastBody = StockForecastBody(
        horizon=1,
        resample="1D",
        test_size=0.2
    )
    response = await test_client.post(
        url=f"api/v1/forecasts/items/{item_mock_data[0].id}/stock",
        json=json.loads(item_stock_forecast.json())
    )
    assert response.status_code == 200
    content: Content[ItemTransactionForecastResponse] = Content[ItemTransactionForecastResponse](**response.json())
    assert type(content.data.metric.mae) == float
    assert type(content.data.metric.smape) == float
    assert type(content.data.prediction.past) == list
    assert type(content.data.prediction.future) == list


@pytest.mark.asyncio
async def test__forecast_item_transaction__should_get_forecast_item_transaction__success():
    item_transaction_forecast: TransactionForecastBody = TransactionForecastBody(
        horizon=1,
        resample="1D",
        test_size=0.2
    )
    response = await test_client.post(
        url=f"api/v1/forecasts/items/{item_mock_data[0].id}/transaction",
        json=json.loads(item_transaction_forecast.json())
    )
    assert response.status_code == 200
    content: Content[ItemTransactionForecastResponse] = Content[ItemTransactionForecastResponse](**response.json())
    assert type(content.data.metric.mae) == float
    assert type(content.data.metric.smape) == float
    assert type(content.data.prediction.past) == list
    assert type(content.data.prediction.future) == list
