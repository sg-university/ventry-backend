from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.role_management.patch_body import PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: PatchBody
