from pydantic import BaseModel


class RolePatch(BaseModel):
    name: str
    description: str
