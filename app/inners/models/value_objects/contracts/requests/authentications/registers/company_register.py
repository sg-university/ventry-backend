from pydantic import BaseModel


class CompanyRegister(BaseModel):
    name: str
    description: str
    address: str
