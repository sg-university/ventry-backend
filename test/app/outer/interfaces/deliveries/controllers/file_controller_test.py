import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.file import File
from app.outers.interfaces.deliveries.contracts.requests.managements.files.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.files.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.file_repository import FileRepository
from test.mock_data.file_mock_data import file_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

file_repository: FileRepository = FileRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for file in file_mock_data:
        await file_repository.create_one(File(**file.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for file in file_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_file__success" \
                and file.id == file_mock_data[0].id:
            continue
        await file_repository.delete_one_by_id(file.id)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_files__success():
    response = await test_client.get(
        url="api/v1/files"
    )
    assert response.status_code == 200
    content: Content[List[File]] = Content[List[File]](**response.json())
    assert all([file in content.data for file in file_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_file__success():
    response = await test_client.get(
        url=f"api/v1/files/{file_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data == file_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_file__success():
    file_create: CreateBody = CreateBody(
        name="name2",
        description="description2",
        extension="extension2",
        content="content2".encode()
    )
    response = await test_client.post(
        url="api/v1/files",
        json=json.loads(file_create.json())
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data.name == file_create.name
    assert content.data.description == file_create.description
    assert content.data.extension == file_create.extension
    assert content.data.content == file_create.content
    file_mock_data.append(content.data)


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_file__success():
    file_patch: PatchBody = PatchBody(
        name=f"{file_mock_data[0].name} patched",
        description=f"{file_mock_data[0].description} patched",
        extension=f"{file_mock_data[0].extension} patched",
        content=f"{file_mock_data[0].content} patched".encode()
    )
    response = await test_client.patch(
        url=f"api/v1/files/{file_mock_data[0].id}",
        json=json.loads(file_patch.json())
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data.name == file_patch.name
    assert content.data.description == file_patch.description
    assert content.data.extension == file_patch.extension
    assert content.data.content == file_patch.content


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_file__success():
    response = await test_client.delete(
        url=f"api/v1/files/{file_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[File] = Content[File](**response.json())
    assert content.data == file_mock_data[0]
