from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.file import File
from app.inner.use_cases.management import file_management
from app.outer.interfaces.deliveries.contracts.requests.file_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.file_create import FileCreate
from app.outer.interfaces.deliveries.contracts.requests.file_management.file_patch import FilePatch
from app.outer.interfaces.deliveries.contracts.requests.file_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.read_one_by_id_request import ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/files", tags=["files"])


@router.get("", response_model=Content[List[File]])
def read_all() -> Content[List[File]]:
    return file_management.read_all()


@router.get("/{id}", response_model=Content[File])
def read_one_by_id(id: UUID) -> Content[File]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return file_management.read_one_by_id(request)


@router.post("", response_model=Content[File])
def create_one(entity: FileCreate) -> Content[File]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return file_management.create_one(request)


@router.patch("/{id}", response_model=Content[File])
def patch_one_by_id(id: UUID, entity: FilePatch) -> Content[File]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return file_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[File])
def delete_one_by_id(id: UUID) -> Content[File]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return file_management.delete_one_by_id(request)
