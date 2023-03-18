import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.account_permission_map import AccountPermissionMap
from app.inners.models.entities.permission import Permission
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories import account_permission_map_repository, role_repository, account_repository, \
    permission_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.account_permission_map_mock_data import account_permission_map_mock_data
from test.mock_data.permission_mock_data import permission_mock_data
from test.mock_data.role_mock_data import role_mock_data
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

    for account_permission_map in account_permission_map_mock_data:
        await account_permission_map_repository.create_one(AccountPermissionMap(**account_permission_map.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for account_permission_map in account_permission_map_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_account_permission_map__success" \
                and account_permission_map.id == account_permission_map_mock_data[0].id:
            continue
        await account_permission_map_repository.delete_one_by_id(account_permission_map.id)

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
async def test__read_all__should_return_all_account_permission_maps__success():
    response = await test_client.get(
        url="api/v1/account-permission-maps"
    )
    assert response.status_code == 200
    content: Content[List[AccountPermissionMap]] = Content[List[AccountPermissionMap]](**response.json())
    assert all([account_permission_map in content.data for account_permission_map in account_permission_map_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_account_permission_map__success():
    response = await test_client.get(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data == account_permission_map_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_account_permission_map__success():
    account_permission_map_create: CreateBody = CreateBody(
        account_id=account_mock_data[0].id,
        permission_id=permission_mock_data[0].id
    )
    response = await test_client.post(
        url="api/v1/account-permission-maps",
        json=json.loads(account_permission_map_create.json())
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data.account_id == account_permission_map_create.account_id
    assert content.data.permission_id == account_permission_map_create.permission_id


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_account_permission_map__success():
    account_permission_map_patch: PatchBody = PatchBody(
        account_id=account_mock_data[1].id,
        permission_id=permission_mock_data[1].id
    )
    response = await test_client.patch(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}",
        json=json.loads(account_permission_map_patch.json())
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data.account_id == account_permission_map_patch.account_id
    assert content.data.permission_id == account_permission_map_patch.permission_id


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_account_permission_map__success():
    response = await test_client.delete(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data == account_permission_map_mock_data[0]
