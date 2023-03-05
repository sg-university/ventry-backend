from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.inventory_control_management.inventory_control_patch_body import \
    InventoryControlPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: InventoryControlPatchBody
