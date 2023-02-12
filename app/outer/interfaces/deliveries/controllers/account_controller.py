from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.account import Account
from app.inner.use_cases.management import account_management
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_create import AccountCreate
from app.outer.interfaces.deliveries.contracts.requests.account_management.account_patch import AccountPatch
from app.outer.interfaces.deliveries.contracts.requests.account_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("", response_model=Content[List[Account]])
def read_all() -> Content[List[Account]]:
    return account_management.read_all()


@router.get("/{id}", response_model=Content[Account])
def read_one_by_id(id: UUID) -> Content[Account]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return account_management.read_one_by_id(request)


@router.post("", response_model=Content[Account])
def create_one(entity: AccountCreate) -> Content[Account]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return account_management.create_one(request)


@router.patch("/{id}", response_model=Content[Account])
def patch_one_by_id(id: UUID, entity: AccountPatch) -> Content[Account]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return account_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Account])
def delete_one_by_id(id: UUID) -> Content[Account]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return account_management.delete_one_by_id(request)
