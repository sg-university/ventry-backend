import json
from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.account import Account
from app.inner.models.entities.file import File
from app.inner.models.entities.item import Item
from app.inner.models.entities.item_file_map import ItemFileMap
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_create import \
    ItemFileMapCreate
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_patch import \
    ItemFileMapPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_file_map_repository, role_repository, account_repository, \
    permission_repository, item_repository, file_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.file_mock_data import file_mock_data
from test.mock_data.item_file_map_mock_data import item_file_map_mock_data
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

    for file in file_mock_data:
        file_repository.create_one(File(**file.dict()))

    for item in item_mock_data:
        item_repository.create_one(Item(**item.dict()))

    for item_file_map in item_file_map_mock_data:
        item_file_map_repository.create_one(ItemFileMap(**item_file_map.dict()))


def teardown_function(function):
    for item_file_map in item_file_map_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_item_file_map__success" \
                and item_file_map.id == item_file_map_mock_data[0].id:
            continue
        item_file_map_repository.delete_one_by_id(item_file_map.id)

    for item in item_mock_data:
        item_repository.delete_one_by_id(item.id)

    for file in file_mock_data:
        file_repository.delete_one_by_id(file.id)

    for permission in permission_mock_data:
        permission_repository.delete_one_by_id(permission.id)

    for account in account_mock_data:
        account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_item_file_maps__success():
    response = test_client.get(
        url="api/v1/item-file-maps"
    )
    assert response.status_code == 200
    content: Content[List[ItemFileMap]] = Content[List[ItemFileMap]](**response.json())
    assert all([item_file_map in content.data for item_file_map in item_file_map_mock_data])


def test__read_one_by_id__should_return_one_item_file_map__success():
    response = test_client.get(
        url=f"api/v1/item-file-maps/{item_file_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemFileMap] = Content[ItemFileMap](**response.json())
    assert content.data == item_file_map_mock_data[0]


def test__create_one__should_create_one_item_file_map__success():
    item_file_map_create: ItemFileMapCreate = ItemFileMapCreate(
        item_id=item_mock_data[0].id,
        file_id=file_mock_data[0].id
    )
    response = test_client.post(
        url="api/v1/item-file-maps",
        json=json.loads(item_file_map_create.json())
    )
    assert response.status_code == 200
    content: Content[ItemFileMap] = Content[ItemFileMap](**response.json())
    assert content.data.item_id == item_file_map_create.item_id
    assert content.data.file_id == item_file_map_create.file_id


def test__patch_one_by_id__should_patch_one_item_file_map__success():
    item_file_map_patch: ItemFileMapPatch = ItemFileMapPatch(
        item_id=item_mock_data[1].id,
        file_id=file_mock_data[1].id
    )
    response = test_client.patch(
        url=f"api/v1/item-file-maps/{item_file_map_mock_data[0].id}",
        json=json.loads(item_file_map_patch.json())
    )
    assert response.status_code == 200
    content: Content[ItemFileMap] = Content[ItemFileMap](**response.json())
    assert content.data.item_id == item_file_map_patch.item_id
    assert content.data.file_id == item_file_map_patch.file_id


def test__delete_one_by_id__should_delete_one_item_file_map__success():
    response = test_client.delete(
        url=f"api/v1/item-file-maps/{item_file_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[ItemFileMap] = Content[ItemFileMap](**response.json())
    assert content.data == item_file_map_mock_data[0]
