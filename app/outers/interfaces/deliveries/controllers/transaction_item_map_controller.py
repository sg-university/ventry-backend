from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.use_cases.managements import transaction_item_map_management
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/transaction-item-maps", tags=["transaction-item-maps"])


@router.get("", response_model=Content[List[TransactionItemMap]])
async def read_all() -> Content[List[TransactionItemMap]]:
    return await transaction_item_map_management.read_all()


@router.get("/{id}", response_model=Content[TransactionItemMap])
async def read_one_by_id(id: UUID) -> Content[TransactionItemMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await transaction_item_map_management.read_one_by_id(request)


@router.post("", response_model=Content[TransactionItemMap])
async def create_one(body: CreateBody) -> Content[TransactionItemMap]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await transaction_item_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[TransactionItemMap])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[TransactionItemMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await transaction_item_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[TransactionItemMap])
async def delete_one_by_id(id: UUID) -> Content[TransactionItemMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await transaction_item_map_management.delete_one_by_id(request)
