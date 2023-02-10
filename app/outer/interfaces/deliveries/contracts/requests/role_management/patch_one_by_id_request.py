from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.role_management.role_patch import RolePatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: RolePatch
