from pydantic import BaseModel


class FileCreate(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
