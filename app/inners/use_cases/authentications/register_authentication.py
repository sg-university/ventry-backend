import uuid

from app.inners.models.entities.account import Account
from app.inners.use_cases.managements import account_management
from app.outers.interfaces.deliveries.contracts.requests.authentications.registers.register_by_email_and_password_request import \
    RegisterByEmailAndPasswordRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_body import CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_one_request import CreateOneRequest
from app.outers.interfaces.deliveries.contracts.responses.authentications.registers.register_response import \
    RegisterResponse
from app.outers.interfaces.deliveries.contracts.responses.content import Content


async def register_by_email_and_password(request: RegisterByEmailAndPasswordRequest) -> Content[RegisterResponse]:
    found_account_by_email: Content[Account] = await account_management.read_one_by_email(request.email)

    if found_account_by_email.data is not None:
        content: Content[RegisterResponse] = Content[RegisterResponse](
            data=None,
            message="Authentication register failed: Email already exists."
        )
        return content

    account_create_body: CreateBody = CreateBody(
        role_id=request.role_id,
        name=request.name,
        email=request.email,
        password=request.password
    )
    account_create_one_request: CreateOneRequest = CreateOneRequest(
        body=account_create_body
    )
    created_account: Content[Account] = await account_management.create_one(account_create_one_request)

    content: Content[RegisterResponse] = Content[RegisterResponse](
        data=RegisterResponse(
            entity=created_account.data
        ),
        message="Authentication register succeed."
    )

    return content
