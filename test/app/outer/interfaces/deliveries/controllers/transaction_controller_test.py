import json
from datetime import datetime
from typing import List

import pytest
import pytest_asyncio

from app.inner.models.entities.account import Account
from app.inner.models.entities.item import Item
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.inner.models.entities.transaction import Transaction
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_create_body import \
    TransactionCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_patch_body import \
    TransactionPatchBody
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import transaction_repository, role_repository, permission_repository, account_repository, \
    item_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.permission_mock_data import permission_mock_data
from test.mock_data.role_mock_data import role_mock_data
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


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for transaction in transaction_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_transaction__success" \
                and transaction.id == transaction_mock_data[0].id:
            continue
        await transaction_repository.delete_one_by_id(transaction.id)

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
async def test__read_all__should_return_all_transactions__success():
    response = await test_client.get(
        url="api/v1/transactions"
    )
    assert response.status_code == 200
    content: Content[List[Transaction]] = Content[List[Transaction]](**response.json())
    assert all([transaction in content.data for transaction in transaction_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_transaction__success():
    response = await test_client.get(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data == transaction_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_transaction__success():
    transaction_create: TransactionCreateBody = TransactionCreateBody(
        account_id=account_mock_data[0].id,
        sell_price=2.0,
        timestamp=datetime.now()
    )
    response = await test_client.post(
        url="api/v1/transactions",
        json=json.loads(transaction_create.json())
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data.account_id == transaction_create.account_id
    assert content.data.sell_price == transaction_create.sell_price
    assert content.data.timestamp == transaction_create.timestamp


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_transaction__success():
    transaction_patch: TransactionPatchBody = TransactionPatchBody(
        account_id=account_mock_data[1].id,
        sell_price=1.0,
        timestamp=datetime.now()
    )
    response = await test_client.patch(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}",
        json=json.loads(transaction_patch.json())
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data.account_id == transaction_patch.account_id
    assert content.data.sell_price == transaction_patch.sell_price
    assert content.data.timestamp == transaction_patch.timestamp


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_transaction__success():
    response = await test_client.delete(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data == transaction_mock_data[0]
