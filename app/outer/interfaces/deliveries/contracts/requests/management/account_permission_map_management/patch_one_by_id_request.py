from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.account_permission_map_patch_body import \
    AccountPermissionMapPatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: AccountPermissionMapPatchBody
