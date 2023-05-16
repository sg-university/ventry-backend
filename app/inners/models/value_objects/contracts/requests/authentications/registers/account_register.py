from pydantic import BaseModel


class AccountRegister(BaseModel):
    name: str
    email: str
    password: str
