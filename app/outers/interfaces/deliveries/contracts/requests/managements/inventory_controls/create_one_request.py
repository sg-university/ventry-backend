from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
