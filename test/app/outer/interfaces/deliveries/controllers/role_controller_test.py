import json
from typing import List

import pytest
import pytest_asyncio

from app.inner.models.entities.role import Role
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.create_body import \
    CreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.patch_body import PatchBody
from app.outer.interfaces.deliveries.contracts.responses.content import Content
from app.outer.repositories import role_repository
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for role in role_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_role__success" \
                and role.id == role_mock_data[0].id:
            continue
        await role_repository.delete_one_by_id(role.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_roles__success():
    response = await test_client.get(
        url="api/v1/roles"
    )
    assert response.status_code == 200
    content: Content[List[Role]] = Content[List[Role]](**response.json())
    assert all([role in content.data for role in role_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_role__success():
    response = await test_client.get(
        url=f"api/v1/roles/{role_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == role_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_role__success():
    role_create: CreateBody = CreateBody(
        name="name2",
        description="description2"
    )
    response = await test_client.post(
        url="api/v1/roles",
        json=json.loads(role_create.json())
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data.name == role_create.name
    assert content.data.description == role_create.description


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_role__success():
    role_patch: PatchBody = PatchBody(
        name=f"{role_mock_data[0].name} patched",
        description=f"{role_mock_data[0].description} patched"
    )
    response = await test_client.patch(
        url=f"api/v1/roles/{role_mock_data[0].id}",
        json=json.loads(role_patch.json())
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data.name == role_patch.name
    assert content.data.description == role_patch.description


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_role__success():
    response = await test_client.delete(
        url=f"api/v1/roles/{role_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == role_mock_data[0]
