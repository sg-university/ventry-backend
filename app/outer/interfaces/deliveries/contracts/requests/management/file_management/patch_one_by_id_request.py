from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.file_management.file_patch_body import FilePatchBody


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: FilePatchBody
