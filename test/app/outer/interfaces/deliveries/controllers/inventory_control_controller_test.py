import json
from datetime import datetime
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.entities.item import Item
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.inventory_control_repository import InventoryControlRepository
from app.outers.repositories.item_repository import ItemRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.inventory_control_mock_data import inventory_control_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
location_repository: LocationRepository = LocationRepository()
account_repository: AccountRepository = AccountRepository()
item_repository: ItemRepository = ItemRepository()
inventory_control_repository: InventoryControlRepository = InventoryControlRepository()


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

    for inventory_control in inventory_control_mock_data:
        await inventory_control_repository.create_one(InventoryControl(**inventory_control.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for inventory_control in inventory_control_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_inventory_control__success" \
                and inventory_control.id == inventory_control_mock_data[0].id:
            continue
        await inventory_control_repository.delete_one_by_id(inventory_control.id)

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
async def test__read_all__should_return_all_inventory_controls__success():
    response = await test_client.get(
        url="api/v1/inventory-controls"
    )
    assert response.status_code == 200
    content: Content[List[InventoryControl]] = Content[List[InventoryControl]](**response.json())
    assert all([inventory_control in content.data for inventory_control in inventory_control_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_inventory_control__success():
    response = await test_client.get(
        url=f"api/v1/inventory-controls/{inventory_control_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[InventoryControl] = Content[InventoryControl](**response.json())
    assert content.data == inventory_control_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_inventory_control__success():
    inventory_control_create: CreateBody = CreateBody(
        account_id=account_mock_data[0].id,
        item_id=item_mock_data[0].id,
        quantity_before=2.0,
        quantity_after=2.0,
        timestamp=datetime.now()
    )
    response = await test_client.post(
        url="api/v1/inventory-controls",
        json=json.loads(inventory_control_create.json())
    )
    assert response.status_code == 200
    content: Content[InventoryControl] = Content[InventoryControl](**response.json())
    assert content.data.account_id == inventory_control_create.account_id
    assert content.data.item_id == inventory_control_create.item_id
    assert content.data.quantity_before == inventory_control_create.quantity_before
    assert content.data.quantity_after == inventory_control_create.quantity_after
    assert content.data.timestamp == inventory_control_create.timestamp


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_inventory_control__success():
    inventory_control_patch: PatchBody = PatchBody(
        account_id=account_mock_data[1].id,
        item_id=item_mock_data[1].id,
        quantity_before=1.0,
        quantity_after=1.0,
        timestamp=datetime.now()
    )
    response = await test_client.patch(
        url=f"api/v1/inventory-controls/{inventory_control_mock_data[0].id}",
        json=json.loads(inventory_control_patch.json())
    )
    assert response.status_code == 200
    content: Content[InventoryControl] = Content[InventoryControl](**response.json())
    assert content.data.account_id == inventory_control_patch.account_id
    assert content.data.item_id == inventory_control_patch.item_id
    assert content.data.quantity_before == inventory_control_patch.quantity_before
    assert content.data.quantity_after == inventory_control_patch.quantity_after
    assert content.data.timestamp == inventory_control_patch.timestamp


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_inventory_control__success():
    response = await test_client.delete(
        url=f"api/v1/inventory-controls/{inventory_control_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[InventoryControl] = Content[InventoryControl](**response.json())
    assert content.data == inventory_control_mock_data[0]
