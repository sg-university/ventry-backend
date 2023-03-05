from pydantic import BaseModel


class FilePatchBody(BaseModel):
    name: str
    description: str
    extension: str
    content: bytes
