from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.file import File
from app.inner.use_cases.management import file_management
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.create_body import \
    CreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.patch_body import PatchBody
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/files", tags=["files"])


@router.get("", response_model=Content[List[File]])
async def read_all() -> Content[List[File]]:
    return await file_management.read_all()


@router.get("/{id}", response_model=Content[File])
async def read_one_by_id(id: UUID) -> Content[File]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await file_management.read_one_by_id(request)


@router.post("", response_model=Content[File])
async def create_one(entity: CreateBody) -> Content[File]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await file_management.create_one(request)


@router.patch("/{id}", response_model=Content[File])
async def patch_one_by_id(id: UUID, entity: PatchBody) -> Content[File]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await file_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[File])
async def delete_one_by_id(id: UUID) -> Content[File]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await file_management.delete_one_by_id(request)
