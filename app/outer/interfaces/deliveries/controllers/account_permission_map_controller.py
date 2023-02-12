from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.inner.use_cases.management import account_permission_map_management
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_create import \
    AccountPermissionMapCreate
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_patch import \
    AccountPermissionMapPatch
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/account-permission-maps", tags=["account-permission-maps"])


@router.get("", response_model=Content[List[AccountPermissionMap]])
def read_all() -> Content[List[AccountPermissionMap]]:
    return account_permission_map_management.read_all()


@router.get("/{id}", response_model=Content[AccountPermissionMap])
def read_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return account_permission_map_management.read_one_by_id(request)


@router.post("", response_model=Content[AccountPermissionMap])
def create_one(entity: AccountPermissionMapCreate) -> Content[AccountPermissionMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return account_permission_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[AccountPermissionMap])
def patch_one_by_id(id: UUID, entity: AccountPermissionMapPatch) -> Content[AccountPermissionMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return account_permission_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[AccountPermissionMap])
def delete_one_by_id(id: UUID) -> Content[AccountPermissionMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return account_permission_map_management.delete_one_by_id(request)
