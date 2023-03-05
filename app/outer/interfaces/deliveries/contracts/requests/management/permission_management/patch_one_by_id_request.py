from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.permission_patch_body import \
    PermissionPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: PermissionPatchBody
