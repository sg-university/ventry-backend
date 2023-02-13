from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.inventory_control_create import \
    InventoryControlCreate


class CreateOneRequest(BaseModel):
    entity: InventoryControlCreate
