from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_patch import \
    AccountPermissionMapPatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: AccountPermissionMapPatch
