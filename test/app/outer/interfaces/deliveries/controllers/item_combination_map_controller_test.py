import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.item import Item
from app.inners.models.entities.item_combination_map import ItemCombinationMap
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.item_combination_map_repository import ItemCombinationMapRepository
from app.outers.repositories.item_repository import ItemRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_combination_map_mock_data import item_combination_map_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
location_repository: LocationRepository = LocationRepository()
account_repository: AccountRepository = AccountRepository()
item_repository: ItemRepository = ItemRepository()
item_combination_map_repository: ItemCombinationMapRepository = ItemCombinationMapRepository()


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

    for item_combination_map in item_combination_map_mock_data:
        await item_combination_map_repository.create_one(ItemCombinationMap(**item_combination_map.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for item_combination_map in item_combination_map_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_item_combination_map__success" \
                and item_combination_map.id == item_combination_map_mock_data[0].id:
            continue
        await item_combination_map_repository.delete_one_by_id(item_combination_map.id)

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
async def test__read_all__should_return_all_item_combination_maps__success():
    response = await test_client.get(
        url="api/v1/item-combination-maps"
    )
    assert response.status_code == 200
    content: Content[List[ItemCombinationMap]] = Content[List[ItemCombinationMap]](**response.json())
    assert all([item_combination_map in content.data for item_combination_map in item_combination_map_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_item_combination_map__success():
    response = await test_client.get(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data == item_combination_map_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_item_combination_map__success():
    item_combination_map_create: CreateBody = CreateBody(
        super_item_id=item_mock_data[0].id,
        sub_item_id=item_mock_data[0].id,
        quantity=0.0
    )
    response = await test_client.post(
        url="api/v1/item-combination-maps",
        json=json.loads(item_combination_map_create.json())
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data.super_item_id == item_combination_map_create.super_item_id
    assert content.data.sub_item_id == item_combination_map_create.sub_item_id
    assert content.data.quantity == item_combination_map_create.quantity


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_item_combination_map__success():
    item_combination_map_patch: PatchBody = PatchBody(
        super_item_id=item_mock_data[1].id,
        sub_item_id=item_mock_data[1].id,
        quantity=1.0
    )
    response = await test_client.patch(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}",
        json=json.loads(item_combination_map_patch.json())
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data.super_item_id == item_combination_map_patch.super_item_id
    assert content.data.sub_item_id == item_combination_map_patch.sub_item_id
    assert content.data.quantity == item_combination_map_patch.quantity


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_item_combination_map__success():
    response = await test_client.delete(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data == item_combination_map_mock_data[0]
