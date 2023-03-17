from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.inventory_control_management.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    entity: CreateBody
