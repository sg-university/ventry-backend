from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
