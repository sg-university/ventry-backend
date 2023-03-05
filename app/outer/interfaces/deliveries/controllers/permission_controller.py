from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.permission import Permission
from app.inner.use_cases.management import permission_management
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.permission_create_body import \
    PermissionCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.permission_patch_body import \
    PermissionPatchBody
from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/permissions", tags=["permissions"])


@router.get("", response_model=Content[List[Permission]])
async def read_all() -> Content[List[Permission]]:
    return await permission_management.read_all()


@router.get("/{id}", response_model=Content[Permission])
async def read_one_by_id(id: UUID) -> Content[Permission]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await permission_management.read_one_by_id(request)


@router.post("", response_model=Content[Permission])
async def create_one(entity: PermissionCreateBody) -> Content[Permission]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await permission_management.create_one(request)


@router.patch("/{id}", response_model=Content[Permission])
async def patch_one_by_id(id: UUID, entity: PermissionPatchBody) -> Content[Permission]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await permission_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Permission])
async def delete_one_by_id(id: UUID) -> Content[Permission]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await permission_management.delete_one_by_id(request)
