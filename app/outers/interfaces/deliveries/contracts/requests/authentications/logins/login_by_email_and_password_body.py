from pydantic import BaseModel


class LoginByEmailAndPasswordBody(BaseModel):
    email: str
    password: str
