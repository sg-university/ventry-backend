from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.account import Account
from app.inner.use_cases.management import account_management
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.account_create_body import \
    AccountCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.account_patch_body import \
    AccountPatchBody
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("", response_model=Content[List[Account]])
async def read_all() -> Content[List[Account]]:
    return await account_management.read_all()


@router.get("/{id}", response_model=Content[Account])
async def read_one_by_id(id: UUID) -> Content[Account]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await account_management.read_one_by_id(request)


@router.post("", response_model=Content[Account])
async def create_one(entity: AccountCreateBody) -> Content[Account]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await account_management.create_one(request)


@router.patch("/{id}", response_model=Content[Account])
async def patch_one_by_id(id: UUID, entity: AccountPatchBody) -> Content[Account]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await account_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Account])
async def delete_one_by_id(id: UUID) -> Content[Account]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await account_management.delete_one_by_id(request)
