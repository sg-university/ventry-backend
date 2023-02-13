from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_create import \
    ItemFileMapCreate


class CreateOneRequest(BaseModel):
    entity: ItemFileMapCreate
