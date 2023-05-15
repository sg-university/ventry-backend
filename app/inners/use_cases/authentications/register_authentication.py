from app.inners.models.entities.account import Account
from app.inners.models.value_objects.contracts.requests.authentications.registers.register_by_email_and_password_request import \
    RegisterByEmailAndPasswordRequest
from app.inners.models.value_objects.contracts.requests.managements.accounts.create_body import CreateBody
from app.inners.models.value_objects.contracts.requests.managements.accounts.create_one_request import CreateOneRequest
from app.inners.models.value_objects.contracts.responses.authentications.registers.register_response import \
    RegisterResponse
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.account_management import AccountManagement


class RegisterAuthentication:
    def __init__(self):
        self.account_management: AccountManagement = AccountManagement()

    async def register_by_email_and_password(self, request: RegisterByEmailAndPasswordRequest) -> Content[
        RegisterResponse]:
        found_account_by_email: Content[Account] = await self.account_management.read_one_by_email(request.email)

        if found_account_by_email.data is not None:
            content: Content[RegisterResponse] = Content[RegisterResponse](
                data=None,
                message="Authentication register failed: Email already exists."
            )
            return content

        account_create_body: CreateBody = CreateBody(
            role_id=request.role_id,
            location_id=request.location_id,
            name=request.name,
            email=request.email,
            password=request.password
        )
        account_create_one_request: CreateOneRequest = CreateOneRequest(
            body=account_create_body
        )
        created_account: Content[Account] = await self.account_management.create_one(account_create_one_request)

        content: Content[RegisterResponse] = Content[RegisterResponse](
            data=RegisterResponse(
                entity=created_account.data
            ),
            message="Authentication register succeed."
        )

        return content
