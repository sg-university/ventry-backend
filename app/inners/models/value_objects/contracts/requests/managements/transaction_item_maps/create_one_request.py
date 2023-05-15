from pydantic import BaseModel

from app.inners.models.value_objects.contracts.requests.managements.transaction_item_maps.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
