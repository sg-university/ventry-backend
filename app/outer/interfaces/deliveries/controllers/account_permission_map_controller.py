from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.inner.use_cases.management import account_permission_map_management
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.create_body import \
    CreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.patch_body import \
    PatchBody
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/account-permission-maps", tags=["account-permission-maps"])


@router.get("", response_model=Content[List[AccountPermissionMap]])
async def read_all() -> Content[List[AccountPermissionMap]]:
    return await account_permission_map_management.read_all()


@router.get("/{id}", response_model=Content[AccountPermissionMap])
async def read_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await account_permission_map_management.read_one_by_id(request)


@router.post("", response_model=Content[AccountPermissionMap])
async def create_one(entity: CreateBody) -> Content[AccountPermissionMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await account_permission_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[AccountPermissionMap])
async def patch_one_by_id(id: UUID, entity: PatchBody) -> Content[AccountPermissionMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await account_permission_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[AccountPermissionMap])
async def delete_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await account_permission_map_management.delete_one_by_id(request)
