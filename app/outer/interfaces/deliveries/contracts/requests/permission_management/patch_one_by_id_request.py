from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_patch import PermissionPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: PermissionPatch
