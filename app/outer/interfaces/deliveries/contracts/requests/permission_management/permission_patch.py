from pydantic import BaseModel


class PermissionPatch(BaseModel):
    name: str
    description: str
