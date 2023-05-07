import json
from typing import List

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.company import Company
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.companies.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.companies.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.company_repository import CompanyRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.company_mock_data import company_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
location_repository: LocationRepository = LocationRepository()
account_repository: AccountRepository = AccountRepository()
company_repository: CompanyRepository = CompanyRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for company in company_mock_data:
        await company_repository.create_one(Company(**company.dict()))

    for location in location_mock_data:
        await location_repository.create_one(Location(**location.dict()))

    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
    print("r", request, "\n")
    for account in account_mock_data:
        print("as", account, "\n")
        if request.node.name == "test__delete_one_by_id__should_delete_one_company__success" \
                and account.id == account_mock_data[0].id:
            continue
        await account_repository.delete_one_by_id(account.id)
        print("ae", account, "\n")

    for role in role_mock_data:
        await role_repository.delete_one_by_id(role.id)

    for location in location_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_company__success" \
                and location.id == location_mock_data[0].id:
            continue
        await location_repository.delete_one_by_id(location.id)

    for company in company_mock_data:
        if request.node.name == "test__delete_one_by_id__should_delete_one_company__success" \
                and company.id == company_mock_data[0].id:
            continue
        await company_repository.delete_one_by_id(company.id)

    if request.node.name == "test__create_one__should_create_one_company__success":
        company_mock_data.pop()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def run_around(request: pytest.FixtureRequest):
    await setup(request)
    yield
    await teardown(request)


@pytest.mark.asyncio
async def test__read_all__should_return_all_companies__success():
    response = await test_client.get(
        url="api/v1/companies"
    )
    assert response.status_code == 200
    content: Content[List[Company]] = Content[List[Company]](**response.json())
    assert all([company in content.data for company in company_mock_data])


@pytest.mark.asyncio
async def test__read_one_by_id__should_return_one_company__success():
    response = await test_client.get(
        url=f"api/v1/companies/{company_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Company] = Content[Company](**response.json())
    assert content.data == company_mock_data[0]


@pytest.mark.asyncio
async def test__read_one_by_account_id__should_return_one_account_company__success():
    response = await test_client.get(
        url=f"api/v1/companies/accounts/{account_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Company] = Content[Company](**response.json())
    assert content.data == company_mock_data[0]


@pytest.mark.asyncio
async def test__create_one__should_create_one_company__success():
    company_create: CreateBody = CreateBody(
        name="name2",
        description="description2",
        address="address2"
    )
    response = await test_client.post(
        url="api/v1/companies",
        json=json.loads(company_create.json())
    )
    assert response.status_code == 200
    content: Content[Company] = Content[Company](**response.json())
    assert content.data.name == company_create.name
    assert content.data.description == company_create.description
    assert content.data.address == company_create.address
    company_mock_data.append(content.data)


@pytest.mark.asyncio
async def test__patch_one_by_id__should_patch_one_company__success():
    company_patch: PatchBody = PatchBody(
        name=f"{company_mock_data[0].name} patched",
        description=f"{company_mock_data[0].description} patched",
        address=f"{company_mock_data[0].address} patched"
    )
    response = await test_client.patch(
        url=f"api/v1/companies/{company_mock_data[0].id}",
        json=json.loads(company_patch.json())
    )
    assert response.status_code == 200
    content: Content[Company] = Content[Company](**response.json())
    assert content.data.name == company_patch.name
    assert content.data.description == company_patch.description
    assert content.data.address == company_patch.address


@pytest.mark.asyncio
async def test__delete_one_by_id__should_delete_one_company__success():
    response = await test_client.delete(
        url=f"api/v1/companies/{company_mock_data[0].id}"
    )
    assert response.status_code == 200
    content: Content[Company] = Content[Company](**response.json())
    assert content.data == company_mock_data[0]
