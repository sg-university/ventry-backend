from app.inners.models.entities.account import Account
from app.inners.use_cases.managements import account_management
from app.outers.interfaces.deliveries.contracts.requests.authentications.logins.login_by_email_and_password_request import \
    LoginByEmailAndPasswordRequest
from app.outers.interfaces.deliveries.contracts.responses.authentications.logins.login_response import LoginResponse
from app.outers.interfaces.deliveries.contracts.responses.content import Content


async def login_by_email_and_password(request: LoginByEmailAndPasswordRequest) -> Content[LoginResponse]:
    found_account_by_email: Content[Account] = await account_management.read_one_by_email(request.email)
    found_account_by_email_and_password: Content[Account] = await account_management.read_one_by_email_and_password(
        request.email,
        request.password)

    if found_account_by_email.data is None:
        content: Content[LoginResponse] = Content[LoginResponse](
            data=None,
            message="Authentication login failed: Email not found."
        )
        return content

    if found_account_by_email_and_password.data is None:
        content: Content[LoginResponse] = Content[LoginResponse](
            data=None,
            message="Authentication login failed: Wrong password."
        )
        return content

    content: Content[LoginResponse] = Content[LoginResponse](
        data=LoginResponse(
            entity=found_account_by_email_and_password.data
        ),
        message="Authentication login succeed."
    )

    return content
