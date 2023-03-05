from pydantic import BaseModel


class RoleCreateBody(BaseModel):
    name: str
    description: str
