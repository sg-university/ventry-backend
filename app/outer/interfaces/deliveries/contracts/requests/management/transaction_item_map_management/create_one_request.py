from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_item_map_management.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    entity: CreateBody
