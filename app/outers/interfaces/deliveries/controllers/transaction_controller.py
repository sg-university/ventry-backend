from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.transaction import Transaction
from app.inners.use_cases.managements import transaction_management
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("", response_model=Content[List[Transaction]])
async def read_all() -> Content[List[Transaction]]:
    return await transaction_management.read_all()


@router.get("/{id}", response_model=Content[Transaction])
async def read_one_by_id(id: UUID) -> Content[Transaction]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await transaction_management.read_one_by_id(request)


@router.post("", response_model=Content[Transaction])
async def create_one(body: CreateBody) -> Content[Transaction]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await transaction_management.create_one(request)


@router.patch("/{id}", response_model=Content[Transaction])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[Transaction]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await transaction_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Transaction])
async def delete_one_by_id(id: UUID) -> Content[Transaction]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await transaction_management.delete_one_by_id(request)
