from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_file_map_management.item_file_map_create_body import \
    ItemFileMapCreateBody


class CreateOneRequest(BaseModel):
    entity: ItemFileMapCreateBody
