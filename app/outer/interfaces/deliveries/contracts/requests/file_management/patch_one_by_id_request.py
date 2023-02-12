from uuid import UUID

from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.file_management.file_patch import FilePatch


class PatchOneByIdRequest(BaseModel):
    id: UUID
    entity: FilePatch
