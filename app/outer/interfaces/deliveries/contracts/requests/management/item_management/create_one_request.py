from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_management.item_create_body import \
    ItemCreateBody


class CreateOneRequest(BaseModel):
    entity: ItemCreateBody
