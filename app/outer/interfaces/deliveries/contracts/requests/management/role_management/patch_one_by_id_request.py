from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.role_management.role_patch_body import RolePatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: RolePatchBody
