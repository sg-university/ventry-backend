from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.inventory_control_management.inventory_control_create_body import \
    InventoryControlCreateBody


class CreateOneRequest(BaseModel):
    entity: InventoryControlCreateBody
