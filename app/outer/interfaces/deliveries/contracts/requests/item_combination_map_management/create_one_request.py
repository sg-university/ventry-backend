from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_create import \
    ItemCombinationMapCreate


class CreateOneRequest(BaseModel):
    entity: ItemCombinationMapCreate
