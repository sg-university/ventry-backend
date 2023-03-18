from pydantic import BaseModel


class LoginByEmailAndPasswordRequest(BaseModel):
    email: str
    password: str
