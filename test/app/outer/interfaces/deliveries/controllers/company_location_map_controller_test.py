import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.company import Company
from app.inners.models.entities.company_location_map import CompanyLocationMap
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.company_location_map_repository import CompanyLocationMapRepository
from app.outers.repositories.company_repository import CompanyRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.company_location_map_mock_data import company_location_map_mock_data
from test.mock_data.company_mock_data import company_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
account_repository: AccountRepository = AccountRepository()
location_repository: LocationRepository = LocationRepository()
company_repository: CompanyRepository = CompanyRepository()
company_location_map_repository: CompanyLocationMapRepository = CompanyLocationMapRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for location in location_mock_data:
        await location_repository.create_one(Location(**location.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))

    for company in company_mock_data:
        await company_repository.create_one(Company(**company.dict()))

    for company_location_map in company_location_map_mock_data:
        await company_location_map_repository.create_one(CompanyLocationMap(**company_location_map.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    for company_location_map in company_location_map_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_company_location_map__success" \
                and company_location_map.id == company_location_map_mock_data[0].id:
            continue
        await company_location_map_repository.delete_one_by_id(company_location_map.id)

    for company in company_mock_data:
        await company_repository.delete_one_by_id(company.id)

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
async def test__read_all__should_return_all_company_location_maps__success():
    response = await test_client.get(
        url="api/v1/company-location-maps"
    )
    assert response.status_code == 200
    content: Content[List[CompanyLocationMap]] = Content[List[CompanyLocationMap]](**response.json())
    assert all([company_location_map in content.data for company_location_map in company_location_map_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_company_location_map__success():
    response = await test_client.get(
        url=f"api/v1/company-location-maps/{company_location_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[CompanyLocationMap] = Content[CompanyLocationMap](**response.json())
    assert content.data == company_location_map_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_company_location_map__success():
    company_location_map_create: CreateBody = CreateBody(
        company_id=company_location_map_mock_data[0].company_id,
        location_id=company_location_map_mock_data[0].location_id,
    )
    response = await test_client.post(
        url="api/v1/company-location-maps",
        json=json.loads(company_location_map_create.json()),
    )
    assert response.status_code == 200
    content: Content[CompanyLocationMap] = Content[CompanyLocationMap](**response.json())
    assert content.data.company_id == company_location_map_create.company_id
    assert content.data.location_id == company_location_map_create.location_id


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_company_location_map__success():
    company_location_map_patch: PatchBody = PatchBody(
        company_id=company_location_map_mock_data[1].company_id,
        location_id=company_location_map_mock_data[1].location_id
    )
    response = await test_client.patch(
        url=f"api/v1/company-location-maps/{company_location_map_mock_data[0].id}",
        json=json.loads(company_location_map_patch.json()),
    )
    assert response.status_code == 200
    content: Content[CompanyLocationMap] = Content[CompanyLocationMap](**response.json())
    assert content.data.company_id == company_location_map_patch.company_id
    assert content.data.location_id == company_location_map_patch.location_id


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_company_location_map__success():
    response = await test_client.delete(
        url=f"api/v1/company-location-maps/{company_location_map_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[CompanyLocationMap] = Content[CompanyLocationMap](**response.json())
    assert content.data == company_location_map_mock_data[0]
