import json
from typing import List

import pytest
import pytest_asyncio

from app.inner.models.entities.account import Account
from app.inner.models.entities.item import Item
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.outer.interfaces.deliveries.contracts.requests.management.item_management.item_create_body import \
    ItemCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.item_management.item_patch_body import ItemPatchBody
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_repository, role_repository, account_repository, permission_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data
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

    for item in item_mock_data:
        await item_repository.create_one(Item(**item.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for item in item_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_item__success" \
                and item.id == item_mock_data[0].id:
            continue
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
async def test__read_all__should_return_all_items__success():
    response = await test_client.get(
        url="api/v1/items"
    )
    assert response.status_code == 200
    content: Content[List[Item]] = Content[List[Item]](**response.json())
    assert all([item in content.data for item in item_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_item__success():
    response = await test_client.get(
        url=f"api/v1/items/{item_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Item] = Content[Item](**response.json())
    assert content.data == item_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_item__success():
    item_create: ItemCreateBody = ItemCreateBody(
        permission_id=item_mock_data[0].permission_id,
        code="code2",
        name="name2",
        description="description2",
        combination_max_quantity=2.0,
        combination_min_quantity=2.0,
        quantity=2.0,
        unit_name="unit_name2",
        unit_sell_price=2.0,
        unit_cost_price=2.0,
    )
    response = await test_client.post(
        url="api/v1/items",
        json=json.loads(item_create.json()),
    )
    assert response.status_code == 200
    content: Content[Item] = Content[Item](**response.json())
    assert content.data.code == item_create.code
    assert content.data.name == item_create.name
    assert content.data.description == item_create.description
    assert content.data.quantity == item_create.quantity
    assert content.data.unit_name == item_create.unit_name
    assert content.data.unit_sell_price == item_create.unit_sell_price
    assert content.data.unit_cost_price == item_create.unit_cost_price


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_item__success():
    item_patch: ItemPatchBody = ItemPatchBody(
        permission_id=item_mock_data[0].permission_id,
        code=f"{item_mock_data[0].code} patched",
        name=f"{item_mock_data[0].name} patched",
        description=f"{item_mock_data[0].description} patched",
        combination_max_quantity=item_mock_data[0].combination_max_quantity + 1.0,
        combination_min_quantity=item_mock_data[0].combination_min_quantity + 1.0,
        quantity=item_mock_data[0].quantity + 1.0,
        unit_name=f"{item_mock_data[0].unit_name} patched",
        unit_sell_price=item_mock_data[0].unit_sell_price + 1.0,
        unit_cost_price=item_mock_data[0].unit_cost_price + 1.0,
    )
    response = await test_client.patch(
        url=f"api/v1/items/{item_mock_data[0].id}",
        json=json.loads(item_patch.json()),
    )
    assert response.status_code == 200
    content: Content[Item] = Content[Item](**response.json())
    assert content.data.code == item_patch.code
    assert content.data.name == item_patch.name
    assert content.data.description == item_patch.description
    assert content.data.quantity == item_patch.quantity
    assert content.data.unit_name == item_patch.unit_name
    assert content.data.unit_sell_price == item_patch.unit_sell_price
    assert content.data.unit_cost_price == item_patch.unit_cost_price


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_item__success():
    response = await test_client.delete(
        url=f"api/v1/items/{item_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Item] = Content[Item](**response.json())
    assert content.data == item_mock_data[0]
