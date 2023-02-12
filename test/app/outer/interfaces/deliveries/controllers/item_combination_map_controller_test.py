from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.account import Account
from app.inner.models.entities.item import Item
from app.inner.models.entities.item_combination_map import ItemCombinationMap
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_create import \
    ItemCombinationMapCreate
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_patch import \
    ItemCombinationMapPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_combination_map_repository, role_repository, account_repository, \
    permission_repository, item_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_combination_map_mock_data import item_combination_map_mock_data
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.permission_mock_data import permission_mock_data
from test.mock_data.role_mock_data import role_mock_data

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

    for item_combination_map in item_combination_map_mock_data:
        item_combination_map_repository.create_one(ItemCombinationMap(**item_combination_map.dict()))


def teardown_function(function):
    for item_combination_map in item_combination_map_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_item_combination_map__success" \
                and item_combination_map.id == item_combination_map_mock_data[0].id:
            continue
        item_combination_map_repository.delete_one_by_id(item_combination_map.id)

    for item in item_mock_data:
        item_repository.delete_one_by_id(item.id)

    for permission in permission_mock_data:
        permission_repository.delete_one_by_id(permission.id)

    for account in account_mock_data:
        account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_item_combination_maps__success():
    response = test_client.get(
        url="api/v1/item-combination-maps"
    )
    assert response.status_code == 200
    content: Content[List[ItemCombinationMap]] = Content[List[ItemCombinationMap]](**response.json())
    assert all([item_combination_map in content.data for item_combination_map in item_combination_map_mock_data])


def test__read_one_by_id__should_return_one_item_combination_map__success():
    response = test_client.get(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data == item_combination_map_mock_data[0]


def test__create_one__should_create_one_item_combination_map__success():
    item_combination_map_create: ItemCombinationMapCreate = ItemCombinationMapCreate(
        super_item_id=item_mock_data[0].id,
        sub_item_id=item_mock_data[0].id,
        quantity=0.0
    )
    response = test_client.post(
        url="api/v1/item-combination-maps",
        data=item_combination_map_create.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data.super_item_id == item_combination_map_create.super_item_id
    assert content.data.sub_item_id == item_combination_map_create.sub_item_id
    assert content.data.quantity == item_combination_map_create.quantity


def test__patch_one_by_id__should_patch_one_item_combination_map__success():
    item_combination_map_patch: ItemCombinationMapPatch = ItemCombinationMapPatch(
        super_item_id=item_mock_data[1].id,
        sub_item_id=item_mock_data[1].id,
        quantity=1.0
    )
    response = test_client.patch(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}",
        data=item_combination_map_patch.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data.super_item_id == item_combination_map_patch.super_item_id
    assert content.data.sub_item_id == item_combination_map_patch.sub_item_id
    assert content.data.quantity == item_combination_map_patch.quantity


def test__delete_one_by_id__should_delete_one_item_combination_map__success():
    response = test_client.delete(
        url=f"api/v1/item-combination-maps/{item_combination_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemCombinationMap] = Content[ItemCombinationMap](**response.json())
    assert content.data == item_combination_map_mock_data[0]
