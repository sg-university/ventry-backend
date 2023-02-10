import uuid
from datetime import datetime
from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.role import Role
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.role_management.role_create import RoleCreate
from app.outer.interfaces.deliveries.contracts.requests.role_management.role_patch import RolePatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import role_repository

test_client = TestClient(app)
# create all integration tests for the role controller

mock_data = [
    Role(id=uuid.uuid4(), name="name0", description="description0", created_at=datetime.now(),
         updated_at=datetime.now()),
    Role(id=uuid.uuid4(), name="name1", description="description1", created_at=datetime.now(),
         updated_at=datetime.now()),
]


def setup_function(function):
    for entity in mock_data:
        role_repository.create_one(Role(**entity.dict()))


def teardown_function(function):
    for entity in mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_role__success" \
                and entity.id == mock_data[0].id:
            return
        role_repository.delete_one_by_id(entity.id)


def test__read_all__should_return_all_roles__success():
    response = test_client.get("api/v1/roles/")
    assert response.status_code == 200
    content: Content[List[Role]] = Content[List[Role]](**response.json())
    assert all([entity in content.data for entity in mock_data])


def test__read_one_by_id__should_return_one_role__success():
    response = test_client.get(f"api/v1/roles/{mock_data[0].id}")
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == mock_data[0]


def test__create_one__should_create_one_role__success():
    entity_create: RoleCreate = RoleCreate(name="name2", description="description2")
    response = test_client.post("api/v1/roles/", json=entity_create.dict())
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    print(content)
    assert content.data.name == entity_create.name
    assert content.data.description == entity_create.description


def test__patch_one_by_id__should_patch_one_role__success():
    entity_patch: RolePatch = RolePatch(name="name0 patched", description="description0 patched")
    response = test_client.patch(f"api/v1/roles/{mock_data[0].id}", json=entity_patch.dict())
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    print(content)
    assert content.data.name == entity_patch.name
    assert content.data.description == entity_patch.description


def test__delete_one_by_id__should_delete_one_role__success():
    response = test_client.delete(f"api/v1/roles/{mock_data[0].id}")
    assert response.status_code == 200
    content: Content[Role] = Content[Role](**response.json())
    assert content.data == mock_data[0]
