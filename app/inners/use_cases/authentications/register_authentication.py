from typing import List

from app.inners.models.entities.account import Account
from app.inners.models.entities.role import Role
from app.inners.models.value_objects.contracts.requests.authentications.registers.register_by_email_and_password_request import \
    RegisterByEmailAndPasswordRequest
from app.inners.models.value_objects.contracts.requests.managements.accounts.create_body import \
    CreateBody as AccountCreateBody
from app.inners.models.value_objects.contracts.requests.managements.accounts.create_one_request import \
    CreateOneRequest as AccountCreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.create_body import \
    CreateBody as CompanyCreateBody
from app.inners.models.value_objects.contracts.requests.managements.companies.create_one_request import \
    CreateOneRequest as CompanyCreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.locations.create_body import \
    CreateBody as LocationCreateBody
from app.inners.models.value_objects.contracts.requests.managements.locations.create_one_request import \
    CreateOneRequest as LocationCreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.roles.read_all_request import \
    ReadAllRequest as RoleReadAllRequest
from app.inners.models.value_objects.contracts.responses.authentications.registers.register_response import \
    RegisterResponse
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.account_management import AccountManagement
from app.inners.use_cases.managements.company_management import CompanyManagement
from app.inners.use_cases.managements.location_management import LocationManagement
from app.inners.use_cases.managements.role_management import RoleManagement


class RegisterAuthentication:
    def __init__(self):
        self.account_management: AccountManagement = AccountManagement()
        self.role_management: RoleManagement = RoleManagement()
        self.location_management: LocationManagement = LocationManagement()
        self.company_management: CompanyManagement = CompanyManagement()

    async def register_by_email_and_password(self, request: RegisterByEmailAndPasswordRequest) -> Content[
        RegisterResponse]:
        found_account_by_email: Content[Account] = await self.account_management.read_one_by_email(
            request.account.email)

        if found_account_by_email.data is not None:
            content: Content[RegisterResponse] = Content[RegisterResponse](
                data=None,
                message="Authentication register failed: Email already exists."
            )
            return content

        found_admin_role: Content[List[Role]] = await self.role_management.read_all(
            RoleReadAllRequest(
                query_parameter={
                    "name": "admin"
                }
            )
        )

        created_company = await self.company_management.create_one(
            CompanyCreateOneRequest(
                body=CompanyCreateBody(
                    name=request.company.name,
                    description=request.company.description,
                    address=request.company.address,
                )
            )
        )

        created_location = await self.location_management.create_one(
            LocationCreateOneRequest(
                body=LocationCreateBody(
                    company_id=created_company.data.id,
                    name=request.location.name,
                    description=request.location.description,
                    address=request.location.address,
                )
            )
        )

        created_account: Content[Account] = await self.account_management.create_one(
            AccountCreateOneRequest(
                body=AccountCreateBody(
                    role_id=found_admin_role.data[0].id,
                    location_id=created_location.data.id,
                    name=request.account.name,
                    email=request.account.email,
                    password=request.account.password
                )
            )
        )

        content: Content[RegisterResponse] = Content[RegisterResponse](
            data=RegisterResponse(
                entity=created_account.data
            ),
            message="Authentication register succeed."
        )

        return content
