from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.transaction import Transaction
from app.inner.use_cases.management import transaction_management
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_create_body import \
    TransactionCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_patch_body import \
    TransactionPatchBody
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("", response_model=Content[List[Transaction]])
async def read_all() -> Content[List[Transaction]]:
    return await transaction_management.read_all()


@router.get("/{id}", response_model=Content[Transaction])
async def read_one_by_id(id: UUID) -> Content[Transaction]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await transaction_management.read_one_by_id(request)


@router.post("", response_model=Content[Transaction])
async def create_one(entity: TransactionCreateBody) -> Content[Transaction]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await transaction_management.create_one(request)


@router.patch("/{id}", response_model=Content[Transaction])
async def patch_one_by_id(id: UUID, entity: TransactionPatchBody) -> Content[Transaction]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await transaction_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Transaction])
async def delete_one_by_id(id: UUID) -> Content[Transaction]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await transaction_management.delete_one_by_id(request)
