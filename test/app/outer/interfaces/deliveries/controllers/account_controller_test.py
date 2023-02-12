from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.account import Account
from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_create import AccountCreate
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_patch import AccountPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import account_repository, role_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.role_mock_data import role_mock_data

test_client = TestClient(app)


def setup_function(function):
    for role in role_mock_data:
        role_repository.create_one(Role(**role.dict()))

    for account in account_mock_data:
        account_repository.create_one(Account(**account.dict()))


def teardown_function(function):
    for account in account_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_account__success" \
                and account.id == account_mock_data[0].id:
            continue
        account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_accounts__success():
    response = test_client.get(
        url="api/v1/accounts"
    )
    assert response.status_code == 200
    content: Content[List[Account]] = Content[List[Account]](**response.json())
    assert all([account in content.data for account in account_mock_data])


def test__read_one_by_id__should_return_one_account__success():
    response = test_client.get(
        url=f"api/v1/accounts/{account_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data == account_mock_data[0]


def test__create_one__should_create_one_account__success():
    account_create: AccountCreate = AccountCreate(
        role_id=role_mock_data[0].id,
        name="name2",
        email="email2",
        password="password2"
    )
    response = test_client.post(
        url="api/v1/accounts",
        data=account_create.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data.role_id == account_create.role_id
    assert content.data.name == account_create.name
    assert content.data.email == account_create.email
    assert content.data.password == account_create.password


def test__patch_one_by_id__should_patch_one_account__success():
    account_patch: AccountPatch = AccountPatch(
        role_id=role_mock_data[1].id,
        name=f"{account_mock_data[0].name} patched",
        email=f"{account_mock_data[0].email} patched",
        password=f"{account_mock_data[0].password} patched"
    )
    response = test_client.patch(
        url=f"api/v1/accounts/{account_mock_data[0].id}",
        data=account_patch.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data.role_id == account_patch.role_id
    assert content.data.name == account_patch.name
    assert content.data.email == account_patch.email
    assert content.data.password == account_patch.password


def test__delete_one_by_id__should_delete_one_account__success():
    response = test_client.delete(
        url=f"api/v1/accounts/{account_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data == account_mock_data[0]
