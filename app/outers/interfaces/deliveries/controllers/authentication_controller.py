from fastapi import APIRouter

from app.inners.use_cases.authentications import login_authentication
from app.inners.use_cases.authentications import register_authentication
from app.outers.interfaces.deliveries.contracts.requests.authentications.logins.login_by_email_and_password_body import \
    LoginByEmailAndPasswordBody
from app.outers.interfaces.deliveries.contracts.requests.authentications.logins.login_by_email_and_password_request import \
    LoginByEmailAndPasswordRequest
from app.outers.interfaces.deliveries.contracts.requests.authentications.registers.register_by_email_and_password_body import \
    RegisterByEmailAndPasswordBody
from app.outers.interfaces.deliveries.contracts.requests.authentications.registers.register_by_email_and_password_request import \
    RegisterByEmailAndPasswordRequest
from app.outers.interfaces.deliveries.contracts.responses.authentications.logins.login_response import LoginResponse
from app.outers.interfaces.deliveries.contracts.responses.authentications.registers.register_response import \
    RegisterResponse
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/authentications", tags=["authentications"])


@router.post("/logins/email-and-password", response_model=Content[LoginResponse])
async def login(body: LoginByEmailAndPasswordBody) -> Content[LoginResponse]:
    request: LoginByEmailAndPasswordRequest = LoginByEmailAndPasswordRequest(
        email=body.email,
        password=body.password
    )
    return await login_authentication.login_by_email_and_password(request)


@router.post("/registers/email-and-password", response_model=Content[RegisterResponse])
async def register(body: RegisterByEmailAndPasswordBody) -> Content[RegisterResponse]:
    request: RegisterByEmailAndPasswordRequest = RegisterByEmailAndPasswordRequest(
        role_id=body.role_id,
        name=body.name,
        email=body.email,
        password=body.password
    )
    return await register_authentication.register_by_email_and_password(request)
