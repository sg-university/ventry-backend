import json
from typing import List

from starlette.testclient import TestClient

from app.inner.models.entities.file import File
from app.main import app
from app.outer.interfaces.deliveries.contracts.requests.file_management.file_create import FileCreate
from app.outer.interfaces.deliveries.contracts.requests.file_management.file_patch import FilePatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import file_repository
from test.mock_data.file_mock_data import file_mock_data

test_client = TestClient(app)


def setup_function(function):
    for file in file_mock_data:
        file_repository.create_one(File(**file.dict()))


def teardown_function(function):
    for file in file_mock_data:
        if function.__name__ == "test__delete_one_by_id__should_delete_one_file__success" \
                and file.id == file_mock_data[0].id:
            continue
        file_repository.delete_one_by_id(file.id)


def test__read_all__should_return_all_files__success():
    response = test_client.get(
        url="api/v1/files"
    )
    assert response.status_code == 200
    content: Content[List[File]] = Content[List[File]](**response.json())
    assert all([file in content.data for file in file_mock_data])


def test__read_one_by_id__should_return_one_file__success():
    response = test_client.get(
        url=f"api/v1/files/{file_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data == file_mock_data[0]


def test__create_one__should_create_one_file__success():
    file_create: FileCreate = FileCreate(
        name="name2",
        description="description2",
        extension="extension2",
        content="content2".encode()
    )
    response = test_client.post(
        url="api/v1/files",
        json=json.loads(file_create.json())
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data.name == file_create.name
    assert content.data.description == file_create.description


def test__patch_one_by_id__should_patch_one_file__success():
    file_patch: FilePatch = FilePatch(
        name=f"{file_mock_data[0].name} patched",
        description=f"{file_mock_data[0].description} patched",
        extension=f"{file_mock_data[0].extension} patched",
        content=f"{file_mock_data[0].content} patched".encode()
    )
    response = test_client.patch(
        url=f"api/v1/files/{file_mock_data[0].id}",
        json=json.loads(file_patch.json())
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data.name == file_patch.name
    assert content.data.description == file_patch.description


def test__delete_one_by_id__should_delete_one_file__success():
    response = test_client.delete(
        url=f"api/v1/files/{file_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data == file_mock_data[0]
