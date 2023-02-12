from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_management.item_create import ItemCreate


class CreateOneRequest(BaseModel):
    entity: ItemCreate
