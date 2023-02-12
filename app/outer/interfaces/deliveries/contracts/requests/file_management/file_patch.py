from pydantic import BaseModel


class FilePatch(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
