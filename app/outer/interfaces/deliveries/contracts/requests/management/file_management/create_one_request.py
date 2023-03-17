from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.file_management.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    entity: CreateBody
