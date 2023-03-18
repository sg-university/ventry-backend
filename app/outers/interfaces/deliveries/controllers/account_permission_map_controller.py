from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.account_permission_map import AccountPermissionMap
from app.inners.use_cases.managements import account_permission_map_management
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.account_permission_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/account-permission-maps", tags=["account-permission-maps"])


@router.get("", response_model=Content[List[AccountPermissionMap]])
async def read_all() -> Content[List[AccountPermissionMap]]:
    return await account_permission_map_management.read_all()


@router.get("/{id}", response_model=Content[AccountPermissionMap])
async def read_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await account_permission_map_management.read_one_by_id(request)


@router.post("", response_model=Content[AccountPermissionMap])
async def create_one(body: CreateBody) -> Content[AccountPermissionMap]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await account_permission_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[AccountPermissionMap])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[AccountPermissionMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await account_permission_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[AccountPermissionMap])
async def delete_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await account_permission_map_management.delete_one_by_id(request)
