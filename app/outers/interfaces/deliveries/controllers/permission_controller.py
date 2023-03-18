from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.permission import Permission
from app.inners.use_cases.managements import permission_management
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.permissions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/permissions", tags=["permissions"])


@router.get("", response_model=Content[List[Permission]])
async def read_all() -> Content[List[Permission]]:
    return await permission_management.read_all()


@router.get("/{id}", response_model=Content[Permission])
async def read_one_by_id(id: UUID) -> Content[Permission]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await permission_management.read_one_by_id(request)


@router.post("", response_model=Content[Permission])
async def create_one(body: CreateBody) -> Content[Permission]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await permission_management.create_one(request)


@router.patch("/{id}", response_model=Content[Permission])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[Permission]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await permission_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Permission])
async def delete_one_by_id(id: UUID) -> Content[Permission]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await permission_management.delete_one_by_id(request)
