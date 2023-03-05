from pydantic import BaseModel


class FileCreateBody(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
