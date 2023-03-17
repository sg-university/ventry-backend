from pydantic import BaseModel


class PatchBody(BaseModel):
    name: str
    description: str
