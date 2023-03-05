from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.item_combination_map_create_body import \
    ItemCombinationMapCreateBody


class CreateOneRequest(BaseModel):
    entity: ItemCombinationMapCreateBody
