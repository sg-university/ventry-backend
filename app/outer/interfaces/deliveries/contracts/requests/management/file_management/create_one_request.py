from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.file_management.file_create_body import \
    FileCreateBody


class CreateOneRequest(BaseModel):
    entity: FileCreateBody
