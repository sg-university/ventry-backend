from pydantic import BaseModel


class PatchBody(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
