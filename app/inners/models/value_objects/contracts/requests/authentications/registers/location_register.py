from pydantic import BaseModel


class LocationRegister(BaseModel):
    name: str
    description: str
    address: str
