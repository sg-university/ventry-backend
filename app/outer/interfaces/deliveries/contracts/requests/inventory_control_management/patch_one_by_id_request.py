from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.inventory_control_patch import \
    InventoryControlPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: InventoryControlPatch
