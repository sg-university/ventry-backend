from pydantic import BaseModel


class RolePatchBody(BaseModel):
    name: str
    description: str
