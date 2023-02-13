from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.transaction import Transaction
from app.inner.use_cases.management import transaction_management
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_create import \
    TransactionCreate
from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_patch import TransactionPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("", response_model=Content[List[Transaction]])
def read_all() -> Content[List[Transaction]]:
    return transaction_management.read_all()


@router.get("/{id}", response_model=Content[Transaction])
def read_one_by_id(id: UUID) -> Content[Transaction]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return transaction_management.read_one_by_id(request)


@router.post("", response_model=Content[Transaction])
def create_one(entity: TransactionCreate) -> Content[Transaction]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return transaction_management.create_one(request)


@router.patch("/{id}", response_model=Content[Transaction])
def patch_one_by_id(id: UUID, entity: TransactionPatch) -> Content[Transaction]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return transaction_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Transaction])
def delete_one_by_id(id: UUID) -> Content[Transaction]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return transaction_management.delete_one_by_id(request)
