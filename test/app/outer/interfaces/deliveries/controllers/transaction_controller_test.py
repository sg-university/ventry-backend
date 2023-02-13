import json
from datetime import datetime
from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.account import Account
from app.inner.models.entities.item import Item
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.inner.models.entities.transaction import Transaction
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_create import \
    TransactionCreate
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_patch import TransactionPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import transaction_repository, role_repository, permission_repository, account_repository, \
    item_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.permission_mock_data import permission_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.mock_data.transaction_mock_data import transaction_mock_data

test_client = TestClient(app)


def setup_function(function):
    for role in role_mock_data:
        role_repository.create_one(Role(**role.dict()))

    for account in account_mock_data:
        account_repository.create_one(Account(**account.dict()))

    for permission in permission_mock_data:
        permission_repository.create_one(Permission(**permission.dict()))

    for item in item_mock_data:
        item_repository.create_one(Item(**item.dict()))

    for transaction in transaction_mock_data:
        transaction_repository.create_one(Transaction(**transaction.dict()))


def teardown_function(function):
    for transaction in transaction_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_transaction__success" \
                and transaction.id == transaction_mock_data[0].id:
            continue
        transaction_repository.delete_one_by_id(transaction.id)

    for item in item_mock_data:
        item_repository.delete_one_by_id(item.id)

    for permission in permission_mock_data:
        permission_repository.delete_one_by_id(permission.id)

    for account in account_mock_data:
        account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_transactions__success():
    response = test_client.get(
        url="api/v1/transactions"
    )
    assert response.status_code == 200
    content: Content[List[Transaction]] = Content[List[Transaction]](**response.json())
    assert all([transaction in content.data for transaction in transaction_mock_data])


def test__read_one_by_id__should_return_one_transaction__success():
    response = test_client.get(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data == transaction_mock_data[0]


def test__create_one__should_create_one_transaction__success():
    transaction_create: TransactionCreate = TransactionCreate(
        account_id=account_mock_data[0].id,
        sell_price=2.0,
        timestamp=datetime.now()
    )
    response = test_client.post(
        url="api/v1/transactions",
        json=json.loads(transaction_create.json())
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data.account_id == transaction_create.account_id
    assert content.data.sell_price == transaction_create.sell_price
    assert content.data.timestamp == transaction_create.timestamp


def test__patch_one_by_id__should_patch_one_transaction__success():
    transaction_patch: TransactionPatch = TransactionPatch(
        account_id=account_mock_data[1].id,
        sell_price=1.0,
        timestamp=datetime.now()
    )
    response = test_client.patch(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}",
        json=json.loads(transaction_patch.json())
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data.account_id == transaction_patch.account_id
    assert content.data.sell_price == transaction_patch.sell_price
    assert content.data.timestamp == transaction_patch.timestamp


def test__delete_one_by_id__should_delete_one_transaction__success():
    response = test_client.delete(
        url=f"api/v1/transactions/{transaction_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Transaction] = Content[Transaction](**response.json())
    assert content.data == transaction_mock_data[0]
