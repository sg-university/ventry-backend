import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.company import Company
from app.inners.models.entities.location import Location
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.company_repository import CompanyRepository
from app.outers.repositories.location_repository import LocationRepository
from test.mock_data.company_mock_data import company_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

location_repository: LocationRepository = LocationRepository()
company_repository: CompanyRepository = CompanyRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for company in company_mock_data:
        await company_repository.create_one(Company(**company.dict()))

    for location in location_mock_data:
        await location_repository.create_one(Location(**location.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for location in location_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_location__success" \
                and location.id == location_mock_data[0].id:
            continue
        await location_repository.delete_one_by_id(location.id)

    for company in company_mock_data:
        await company_repository.delete_one_by_id(company.id)

    if request.node.name == "test__create_one__should_create_one_location__success":
        location_mock_data.pop()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_locations__success():
    response = await test_client.get(
        url="api/v1/locations"
    )
    assert response.status_code == 200
    content: Content[List[Location]] = Content[List[Location]](**response.json())
    assert all([location in content.data for location in location_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_location__success():
    response = await test_client.get(
        url=f"api/v1/locations/{location_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Location] = Content[Location](**response.json())
    assert content.data == location_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_location__success():
    location_create: CreateBody = CreateBody(
        company_id=company_mock_data[0].id,
        name="name2",
        description="description2",
        address="address2"
    )
    response = await test_client.post(
        url="api/v1/locations",
        json=json.loads(location_create.json())
    )
    assert response.status_code == 200
    content: Content[Location] = Content[Location](**response.json())
    assert content.data.company_id == location_create.company_id
    assert content.data.name == location_create.name
    assert content.data.description == location_create.description
    location_mock_data.append(content.data)


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_location__success():
    location_patch: PatchBody = PatchBody(
        company_id=company_mock_data[1].id,
        name=f"{location_mock_data[0].name} patched",
        description=f"{location_mock_data[0].description} patched",
        address=f"{location_mock_data[0].address} patched"
    )
    response = await test_client.patch(
        url=f"api/v1/locations/{location_mock_data[0].id}",
        json=json.loads(location_patch.json())
    )
    assert response.status_code == 200
    content: Content[Location] = Content[Location](**response.json())
    assert content.data.company_id == location_patch.company_id
    assert content.data.name == location_patch.name
    assert content.data.description == location_patch.description


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_location__success():
    response = await test_client.delete(
        url=f"api/v1/locations/{location_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Location] = Content[Location](**response.json())
    assert content.data == location_mock_data[0]
