import json
from typing import List

import pytest
import pytest_asyncio

from app.inner.models.entities.permission import Permission
from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_create import PermissionCreate
from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_patch import PermissionPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import permission_repository
from test.mock_data.permission_mock_data import permission_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for permission in permission_mock_data:
        await permission_repository.create_one(Permission(**permission.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for permission in permission_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_permission__success" \
                and permission.id == permission_mock_data[0].id:
            continue
        await permission_repository.delete_one_by_id(permission.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_permissions__success():
    response = await test_client.get(
        url="api/v1/permissions"
    )
    assert response.status_code == 200
    content: Content[List[Permission]] = Content[List[Permission]](**response.json())
    assert all([permission in content.data for permission in permission_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_permission__success():
    response = await test_client.get(
        url=f"api/v1/permissions/{permission_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data == permission_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_permission__success():
    permission_create: PermissionCreate = PermissionCreate(
        name="name2",
        description="description2"
    )
    response = await test_client.post(
        url="api/v1/permissions",
        json=json.loads(permission_create.json())
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data.name == permission_create.name
    assert content.data.description == permission_create.description


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_permission__success():
    permission_patch: PermissionPatch = PermissionPatch(
        name=f"{permission_mock_data[0].name} patched",
        description=f"{permission_mock_data[0].description} patched"
    )
    response = await test_client.patch(
        url=f"api/v1/permissions/{permission_mock_data[0].id}",
        json=json.loads(permission_patch.json())
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data.name == permission_patch.name
    assert content.data.description == permission_patch.description


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_permission__success():
    response = await test_client.delete(
        url=f"api/v1/permissions/{permission_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data == permission_mock_data[0]
