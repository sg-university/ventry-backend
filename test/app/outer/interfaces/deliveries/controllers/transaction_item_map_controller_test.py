import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.item import Item
from app.inners.models.entities.permission import Permission
from app.inners.models.entities.role import Role
from app.inners.models.entities.transaction import Transaction
from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories import transaction_item_map_repository, role_repository, permission_repository, \
    account_repository, \
    item_repository, transaction_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.permission_mock_data import permission_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.mock_data.transaction_item_map_mock_data import transaction_item_map_mock_data
from test.mock_data.transaction_mock_data import transaction_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))

    for permission in permission_mock_data:
        await permission_repository.create_one(Permission(**permission.dict()))

    for item in item_mock_data:
        await item_repository.create_one(Item(**item.dict()))

    for transaction in transaction_mock_data:
        await transaction_repository.create_one(Transaction(**transaction.dict()))

    for transaction_item_map in transaction_item_map_mock_data:
        await transaction_item_map_repository.create_one(TransactionItemMap(**transaction_item_map.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for transaction_item_map in transaction_item_map_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_transaction_item_map__success" \
                and transaction_item_map.id == transaction_item_map_mock_data[0].id:
            continue
        await transaction_item_map_repository.delete_one_by_id(transaction_item_map.id)

    for item in item_mock_data:
        await item_repository.delete_one_by_id(item.id)

    for permission in permission_mock_data:
        await permission_repository.delete_one_by_id(permission.id)

    for account in account_mock_data:
        await account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        await role_repository.delete_one_by_id(role.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_transaction_item_maps__success():
    response = await test_client.get(
        url="api/v1/transaction-item-maps"
    )
    assert response.status_code == 200
    content: Content[List[TransactionItemMap]] = Content[List[TransactionItemMap]](**response.json())
    assert all([transaction_item_map in content.data for transaction_item_map in transaction_item_map_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_transaction_item_map__success():
    response = await test_client.get(
        url=f"api/v1/transaction-item-maps/{transaction_item_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[TransactionItemMap] = Content[TransactionItemMap](**response.json())
    assert content.data == transaction_item_map_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_transaction_item_map__success():
    transaction_item_map_create: CreateBody = CreateBody(
        transaction_id=transaction_mock_data[0].id,
        item_id=item_mock_data[0].id,
        quantity=2.0,
        sell_price=2.0
    )
    response = await test_client.post(
        url="api/v1/transaction-item-maps",
        json=json.loads(transaction_item_map_create.json())
    )
    assert response.status_code == 200
    content: Content[TransactionItemMap] = Content[TransactionItemMap](**response.json())
    assert content.data.transaction_id == transaction_item_map_create.transaction_id
    assert content.data.item_id == transaction_item_map_create.item_id
    assert content.data.quantity == transaction_item_map_create.quantity
    assert content.data.sell_price == transaction_item_map_create.sell_price


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_transaction_item_map__success():
    transaction_item_map_patch: PatchBody = PatchBody(
        transaction_id=transaction_mock_data[1].id,
        item_id=item_mock_data[1].id,
        quantity=1.0,
        sell_price=1.0
    )
    response = await test_client.patch(
        url=f"api/v1/transaction-item-maps/{transaction_item_map_mock_data[0].id}",
        json=json.loads(transaction_item_map_patch.json())
    )
    assert response.status_code == 200
    content: Content[TransactionItemMap] = Content[TransactionItemMap](**response.json())
    assert content.data.transaction_id == transaction_item_map_patch.transaction_id
    assert content.data.item_id == transaction_item_map_patch.item_id
    assert content.data.quantity == transaction_item_map_patch.quantity
    assert content.data.sell_price == transaction_item_map_patch.sell_price


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_transaction_item_map__success():
    response = await test_client.delete(
        url=f"api/v1/transaction-item-maps/{transaction_item_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[TransactionItemMap] = Content[TransactionItemMap](**response.json())
    assert content.data == transaction_item_map_mock_data[0]
