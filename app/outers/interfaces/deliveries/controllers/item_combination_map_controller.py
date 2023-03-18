from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.item_combination_map import ItemCombinationMap
from app.inners.use_cases.managements import item_combination_map_management
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/item-combination-maps", tags=["item-combination-maps"])


@router.get("", response_model=Content[List[ItemCombinationMap]])
async def read_all() -> Content[List[ItemCombinationMap]]:
    return await item_combination_map_management.read_all()


@router.get("/{id}", response_model=Content[ItemCombinationMap])
async def read_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_combination_map_management.read_one_by_id(request)


@router.post("", response_model=Content[ItemCombinationMap])
async def create_one(body: CreateBody) -> Content[ItemCombinationMap]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await item_combination_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[ItemCombinationMap])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[ItemCombinationMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await item_combination_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[ItemCombinationMap])
async def delete_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_combination_map_management.delete_one_by_id(request)
