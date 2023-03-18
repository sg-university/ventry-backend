from uuid import UUID

from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_body import PatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    body: PatchBody
