from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.account import Account
from app.inners.use_cases.managements import account_management
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("", response_model=Content[List[Account]])
async def read_all() -> Content[List[Account]]:
    return await account_management.read_all()


@router.get("/{id}", response_model=Content[Account])
async def read_one_by_id(id: UUID) -> Content[Account]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await account_management.read_one_by_id(request)


@router.post("", response_model=Content[Account])
async def create_one(body: CreateBody) -> Content[Account]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await account_management.create_one(request)


@router.patch("/{id}", response_model=Content[Account])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[Account]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await account_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Account])
async def delete_one_by_id(id: UUID) -> Content[Account]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await account_management.delete_one_by_id(request)
