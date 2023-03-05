from pydantic import BaseModel


class PermissionPatchBody(BaseModel):
    name: str
    description: str
