from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
