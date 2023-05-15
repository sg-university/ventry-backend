from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.file import File
from app.inners.models.value_objects.contracts.requests.managements.files.create_body import \
    CreateBody
from app.inners.models.value_objects.contracts.requests.managements.files.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.files.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.files.patch_body import \
    PatchBody
from app.inners.models.value_objects.contracts.requests.managements.files.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.files.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.files.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.file_management import FileManagement

router: APIRouter = APIRouter(tags=["files"])


@cbv(router)
class FileController:
    def __init__(self):
        self.file_management: FileManagement = FileManagement()

    @router.get("/files")
    async def read_all(self, request: Request) -> Content[List[File]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.file_management.read_all(request=request)

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
