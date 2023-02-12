from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.account import Account
from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.inner.models.entities.permission import Permission
from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_create import \
    AccountPermissionMapCreate
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_patch import \
    AccountPermissionMapPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import account_permission_map_repository, role_repository, account_repository, \
    permission_repository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.account_permission_map_mock_data import account_permission_map_mock_data
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

    for account_permission_map in account_permission_map_mock_data:
        account_permission_map_repository.create_one(AccountPermissionMap(**account_permission_map.dict()))


def teardown_function(function):
    for account_permission_map in account_permission_map_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_account_permission_map__success" \
                and account_permission_map.id == account_permission_map_mock_data[0].id:
            continue
        account_permission_map_repository.delete_one_by_id(account_permission_map.id)

    for permission in permission_mock_data:
        permission_repository.delete_one_by_id(permission.id)

    for account in account_mock_data:
        account_repository.delete_one_by_id(account.id)

    for role in role_mock_data:
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_account_permission_maps__success():
    response = test_client.get(
        url="api/v1/account-permission-maps"
    )
    assert response.status_code == 200
    content: Content[List[AccountPermissionMap]] = Content[List[AccountPermissionMap]](**response.json())
    assert all([account_permission_map in content.data for account_permission_map in account_permission_map_mock_data])


def test__read_one_by_id__should_return_one_account_permission_map__success():
    response = test_client.get(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data == account_permission_map_mock_data[0]


def test__create_one__should_create_one_account_permission_map__success():
    account_permission_map_create: AccountPermissionMapCreate = AccountPermissionMapCreate(
        account_id=account_mock_data[0].id,
        permission_id=permission_mock_data[0].id
    )
    response = test_client.post(
        url="api/v1/account-permission-maps",
        data=account_permission_map_create.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data.account_id == account_permission_map_create.account_id
    assert content.data.permission_id == account_permission_map_create.permission_id


def test__patch_one_by_id__should_patch_one_account_permission_map__success():
    account_permission_map_patch: AccountPermissionMapPatch = AccountPermissionMapPatch(
        account_id=account_mock_data[1].id,
        permission_id=permission_mock_data[1].id
    )
    response = test_client.patch(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}",
        data=account_permission_map_patch.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data.account_id == account_permission_map_patch.account_id
    assert content.data.permission_id == account_permission_map_patch.permission_id


def test__delete_one_by_id__should_delete_one_account_permission_map__success():
    response = test_client.delete(
        url=f"api/v1/account-permission-maps/{account_permission_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[AccountPermissionMap] = Content[AccountPermissionMap](**response.json())
    assert content.data == account_permission_map_mock_data[0]
