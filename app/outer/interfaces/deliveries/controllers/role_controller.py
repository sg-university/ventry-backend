from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.role import Role
from app.inner.use_cases.management import role_management
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.role_create_body import \
    RoleCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.role_management.role_patch_body import RolePatchBody
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/roles", tags=["roles"])


@router.get("", response_model=Content[List[Role]])
async def read_all() -> Content[List[Role]]:
    return await role_management.read_all()


@router.get("/{id}", response_model=Content[Role])
async def read_one_by_id(id: UUID) -> Content[Role]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await role_management.read_one_by_id(request)


@router.post("", response_model=Content[Role])
async def create_one(entity: RoleCreateBody) -> Content[Role]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await role_management.create_one(request)


@router.patch("/{id}", response_model=Content[Role])
async def patch_one_by_id(id: UUID, entity: RolePatchBody) -> Content[Role]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await role_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Role])
async def delete_one_by_id(id: UUID) -> Content[Role]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await role_management.delete_one_by_id(request)
