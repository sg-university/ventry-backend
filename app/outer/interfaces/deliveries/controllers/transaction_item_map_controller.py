from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.transaction_item_map import TransactionItemMap
from app.inner.use_cases.management import transaction_item_map_management
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.transaction_item_map_create import \
    TransactionItemMapCreate
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.transaction_item_map_patch import \
    TransactionItemMapPatch
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/transaction-item-maps", tags=["transaction-item-maps"])


@router.get("", response_model=Content[List[TransactionItemMap]])
def read_all() -> Content[List[TransactionItemMap]]:
    return transaction_item_map_management.read_all()


@router.get("/{id}", response_model=Content[TransactionItemMap])
def read_one_by_id(id: UUID) -> Content[TransactionItemMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return transaction_item_map_management.read_one_by_id(request)


@router.post("", response_model=Content[TransactionItemMap])
def create_one(entity: TransactionItemMapCreate) -> Content[TransactionItemMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return transaction_item_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[TransactionItemMap])
def patch_one_by_id(id: UUID, entity: TransactionItemMapPatch) -> Content[TransactionItemMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return transaction_item_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[TransactionItemMap])
def delete_one_by_id(id: UUID) -> Content[TransactionItemMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return transaction_item_map_management.delete_one_by_id(request)
