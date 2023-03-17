from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_management.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    entity: CreateBody
