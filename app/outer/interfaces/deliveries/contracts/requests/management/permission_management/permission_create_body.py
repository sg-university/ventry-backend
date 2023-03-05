from pydantic import BaseModel


class PermissionCreateBody(BaseModel):
    name: str
    description: str
