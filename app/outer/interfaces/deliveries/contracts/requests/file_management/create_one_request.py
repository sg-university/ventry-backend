from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.file_management.file_create import FileCreate


class CreateOneRequest(BaseModel):
    entity: FileCreate
