from pydantic import BaseModel


class CreateBody(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
