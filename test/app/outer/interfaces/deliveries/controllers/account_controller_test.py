import json
from typing import List

import pytest
import pytest_asyncio

from app.inner.models.entities.account import Account
from app.inner.models.entities.role import Role
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_create import AccountCreate
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_patch import AccountPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import account_repository, role_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for account in account_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_account__success" \
                and account.id == account_mock_data[0].id:
            continue
        await account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        await role_repository.delete_one_by_id(role.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_accounts__success():
    response = await test_client.get(
        url="api/v1/accounts"
    )
    assert response.status_code == 200
    content: Content[List[Account]] = Content[List[Account]](**response.json())
    assert all([account in content.data for account in account_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_account__success():
    response = await test_client.get(
        url=f"api/v1/accounts/{account_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data == account_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_account__success():
    account_create: AccountCreate = AccountCreate(
        role_id=role_mock_data[0].id,
        name="name2",
        email="email2",
        password="password2"
    )
    response = await test_client.post(
        url="api/v1/accounts",
        json=json.loads(account_create.json())
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data.role_id == account_create.role_id
    assert content.data.name == account_create.name
    assert content.data.email == account_create.email
    assert content.data.password == account_create.password


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_account__success():
    account_patch: AccountPatch = AccountPatch(
        role_id=role_mock_data[1].id,
        name=f"{account_mock_data[0].name} patched",
        email=f"{account_mock_data[0].email} patched",
        password=f"{account_mock_data[0].password} patched"
    )
    response = await test_client.patch(
        url=f"api/v1/accounts/{account_mock_data[0].id}",
        json=json.loads(account_patch.json())
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data.role_id == account_patch.role_id
    assert content.data.name == account_patch.name
    assert content.data.email == account_patch.email
    assert content.data.password == account_patch.password


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_account__success():
    response = await test_client.delete(
        url=f"api/v1/accounts/{account_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Account] = Content[Account](**response.json())
    assert content.data == account_mock_data[0]
