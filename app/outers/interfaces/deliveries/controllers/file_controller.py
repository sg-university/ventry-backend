from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.file import File
from app.inners.use_cases.managements.file_management import FileManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.files.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.files.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.files.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["files"])


@cbv(router)
class FileController:
    def __init__(self):
        self.file_management: FileManagement = FileManagement()

    @router.get("/files")
    async def read_all(self) -> Content[List[File]]:
        return await self.file_management.read_all()

    @router.get("/files/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[File]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.file_management.read_one_by_id(request)

    @router.post("/files")
    async def create_one(self, body: CreateBody) -> Content[File]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.file_management.create_one(request)

    @router.patch("/files/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[File]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.file_management.patch_one_by_id(request)

    @router.delete("/files/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[File]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.file_management.delete_one_by_id(request)
