import json

import pytest
import pytest_asyncio

from app.inners.models.entities.account import Account
from app.inners.models.entities.location import Location
from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.authentications.logins.login_by_email_and_password_body import \
    LoginByEmailAndPasswordBody
from app.outers.interfaces.deliveries.contracts.requests.authentications.registers.register_by_email_and_password_body import \
    RegisterByEmailAndPasswordBody
from app.outers.interfaces.deliveries.contracts.responses.authentications.logins.login_response import LoginResponse
from app.outers.interfaces.deliveries.contracts.responses.authentications.registers.register_response import \
    RegisterResponse
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.account_repository import AccountRepository
from app.outers.repositories.location_repository import LocationRepository
from app.outers.repositories.role_repository import RoleRepository
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data
from test.utilities.test_client_utility import get_async_client

test_client = get_async_client()

role_repository: RoleRepository = RoleRepository()
location_repository: LocationRepository = LocationRepository()
account_repository: AccountRepository = AccountRepository()


@pytest.mark.asyncio
async def setup(request: pytest.FixtureRequest):
    for role in role_mock_data:
        await role_repository.create_one(Role(**role.dict()))

    for location in location_mock_data:
        await location_repository.create_one(Location(**location.dict()))

    for account in account_mock_data:
        await account_repository.create_one(Account(**account.dict()))


@pytest.mark.asyncio
async def teardown(request: pytest.FixtureRequest):
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
async def test__login_by_email_and_password__should_logon__success():
    login_by_email_and_password: LoginByEmailAndPasswordBody = LoginByEmailAndPasswordBody(
        email=account_mock_data[0].email,
        password=account_mock_data[0].password
    )
    response = await test_client.post(
        url="api/v1/authentications/logins/email-and-password",
        json=json.loads(login_by_email_and_password.json())
    )
    assert response.status_code == 200
    content: Content[LoginResponse] = Content[LoginResponse](**response.json())
    assert content.data is not None
    assert content.data.entity == account_mock_data[0]


@pytest.mark.asyncio
async def test__login_by_email_and_wrong_password__should_did_not_logon__failed():
    login_by_email_and_password: LoginByEmailAndPasswordBody = LoginByEmailAndPasswordBody(
        email=account_mock_data[0].email,
        password="wrong_password"
    )
    response = await test_client.post(
        url="api/v1/authentications/logins/email-and-password",
        json=json.loads(login_by_email_and_password.json())
    )
    assert response.status_code == 200
    content: Content[LoginResponse] = Content[LoginResponse](**response.json())
    assert content.data is None


@pytest.mark.asyncio
async def test__login_by_not_existed_email_and_password__should_did_not_logon__failed():
    login_by_email_and_password: LoginByEmailAndPasswordBody = LoginByEmailAndPasswordBody(
        email="not_existed_email@domain",
        password=account_mock_data[0].password
    )
    response = await test_client.post(
        url="api/v1/authentications/logins/email-and-password",
        json=json.loads(login_by_email_and_password.json())
    )
    assert response.status_code == 200
    content: Content[LoginResponse] = Content[LoginResponse](**response.json())
    assert content.data is None


@pytest.mark.asyncio
async def test__register_by_email_and_password__should_register__success():
    register_by_email_and_password: RegisterByEmailAndPasswordBody = RegisterByEmailAndPasswordBody(
        role_id=role_mock_data[0].id,
        location_id=location_mock_data[0].id,
        name="name",
        email="email@domain",
        password="password",
    )

    response = await test_client.post(
        url="api/v1/authentications/registers/email-and-password",
        json=json.loads(register_by_email_and_password.json())
    )
    assert response.status_code == 200
    content: Content[RegisterResponse] = Content[RegisterResponse](**response.json())
    assert content.data is not None
    assert content.data.entity.role_id == register_by_email_and_password.role_id
    assert content.data.entity.location_id == register_by_email_and_password.location_id
    assert content.data.entity.name == register_by_email_and_password.name
    assert content.data.entity.email == register_by_email_and_password.email
    assert content.data.entity.password == register_by_email_and_password.password


@pytest.mark.asyncio
async def test__register_by_existed_email__should_did_not_register__failed():
    register_by_email_and_password: RegisterByEmailAndPasswordBody = RegisterByEmailAndPasswordBody(
        role_id=role_mock_data[0].id,
        location_id=location_mock_data[0].id,
        name="name",
        email=account_mock_data[0].email,
        password="password",
    )

    response = await test_client.post(
        url="api/v1/authentications/registers/email-and-password",
        json=json.loads(register_by_email_and_password.json())
    )
    assert response.status_code == 200
    content: Content[RegisterResponse] = Content[RegisterResponse](**response.json())
    assert content.data is None
