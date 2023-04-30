from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
