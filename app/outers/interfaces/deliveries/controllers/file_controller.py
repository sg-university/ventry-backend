from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.file import File
from app.inners.use_cases.managements import file_management
from app.outers.interfaces.deliveries.contracts.requests.managements.files.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.files.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.files.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.files.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/files", tags=["files"])


@router.get("", response_model=Content[List[File]])
async def read_all() -> Content[List[File]]:
    return await file_management.read_all()


@router.get("/{id}", response_model=Content[File])
async def read_one_by_id(id: UUID) -> Content[File]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await file_management.read_one_by_id(request)


@router.post("", response_model=Content[File])
async def create_one(body: CreateBody) -> Content[File]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await file_management.create_one(request)


@router.patch("/{id}", response_model=Content[File])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[File]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await file_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[File])
async def delete_one_by_id(id: UUID) -> Content[File]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await file_management.delete_one_by_id(request)
