from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.role_management.role_create import RoleCreate
from app.outer.interfaces.deliveries.contracts.requests.role_management.role_patch import RolePatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import role_repository
from test.mock_data.role_mock_data import role_mock_data

test_client = TestClient(app)


def setup_function(function):
    for role in role_mock_data:
        role_repository.create_one(Role(**role.dict()))


def teardown_function(function):
    for role in role_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_role__success" \
                and role.id == role_mock_data[0].id:
            continue
        role_repository.delete_one_by_id(role.id)


def test__read_all__should_return_all_roles__success():
    response = test_client.get(
        url="api/v1/roles"
    )
    assert response.status_code == 200
    content: Content[List[Role]] = Content[List[Role]](**response.json())
    assert all([role in content.data for role in role_mock_data])


def test__read_one_by_id__should_return_one_role__success():
    response = test_client.get(
        url=f"api/v1/roles/{role_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == role_mock_data[0]


def test__create_one__should_create_one_role__success():
    role_create: RoleCreate = RoleCreate(
        name="name2",
        description="description2"
    )
    response = test_client.post(
        url="api/v1/roles",
        data=role_create.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data.name == role_create.name
    assert content.data.description == role_create.description


def test__patch_one_by_id__should_patch_one_role__success():
    role_patch: RolePatch = RolePatch(
        name=f"{role_mock_data[0].name} patched",
        description=f"{role_mock_data[0].description} patched"
    )
    response = test_client.patch(
        url=f"api/v1/roles/{role_mock_data[0].id}",
        data=role_patch.json(),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data.name == role_patch.name
    assert content.data.description == role_patch.description


def test__delete_one_by_id__should_delete_one_role__success():
    response = test_client.delete(
        url=f"api/v1/roles/{role_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == role_mock_data[0]
