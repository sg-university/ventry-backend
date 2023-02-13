import json
from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.permission import Permission
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_create import PermissionCreate
from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_patch import PermissionPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import permission_repository
from test.mock_data.permission_mock_data import permission_mock_data

test_client = TestClient(app)


def setup_function(function):
    for permission in permission_mock_data:
        permission_repository.create_one(Permission(**permission.dict()))


def teardown_function(function):
    for permission in permission_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_permission__success" \
                and permission.id == permission_mock_data[0].id:
            continue
        permission_repository.delete_one_by_id(permission.id)


def test__read_all__should_return_all_permissions__success():
    response = test_client.get(
        url="api/v1/permissions"
    )
    assert response.status_code == 200
    content: Content[List[Permission]] = Content[List[Permission]](**response.json())
    assert all([permission in content.data for permission in permission_mock_data])


def test__read_one_by_id__should_return_one_permission__success():
    response = test_client.get(
        url=f"api/v1/permissions/{permission_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data == permission_mock_data[0]


def test__create_one__should_create_one_permission__success():
    permission_create: PermissionCreate = PermissionCreate(
        name="name2",
        description="description2"
    )
    response = test_client.post(
        url="api/v1/permissions",
        json=json.loads(permission_create.json())
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data.name == permission_create.name
    assert content.data.description == permission_create.description


def test__patch_one_by_id__should_patch_one_permission__success():
    permission_patch: PermissionPatch = PermissionPatch(
        name=f"{permission_mock_data[0].name} patched",
        description=f"{permission_mock_data[0].description} patched"
    )
    response = test_client.patch(
        url=f"api/v1/permissions/{permission_mock_data[0].id}",
        json=json.loads(permission_patch.json())
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data.name == permission_patch.name
    assert content.data.description == permission_patch.description


def test__delete_one_by_id__should_delete_one_permission__success():
    response = test_client.delete(
        url=f"api/v1/permissions/{permission_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Permission] = Content[Permission](**response.json())
    assert content.data == permission_mock_data[0]
