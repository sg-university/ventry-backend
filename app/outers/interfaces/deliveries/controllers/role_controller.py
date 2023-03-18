from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.role import Role
from app.inners.use_cases.managements import role_management
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/roles", tags=["roles"])


@router.get("", response_model=Content[List[Role]])
async def read_all() -> Content[List[Role]]:
    return await role_management.read_all()


@router.get("/{id}", response_model=Content[Role])
async def read_one_by_id(id: UUID) -> Content[Role]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await role_management.read_one_by_id(request)


@router.post("", response_model=Content[Role])
async def create_one(body: CreateBody) -> Content[Role]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await role_management.create_one(request)


@router.patch("/{id}", response_model=Content[Role])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[Role]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await role_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Role])
async def delete_one_by_id(id: UUID) -> Content[Role]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await role_management.delete_one_by_id(request)
