from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.item_combination_map import ItemCombinationMap
from app.inner.use_cases.management import item_combination_map_management
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.item_combination_map_create_body import \
    ItemCombinationMapCreateBody
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.item_combination_map_patch_body import \
    ItemCombinationMapPatchBody
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.item_combination_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/item-combination-maps", tags=["item-combination-maps"])


@router.get("", response_model=Content[List[ItemCombinationMap]])
async def read_all() -> Content[List[ItemCombinationMap]]:
    return await item_combination_map_management.read_all()


@router.get("/{id}", response_model=Content[ItemCombinationMap])
async def read_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_combination_map_management.read_one_by_id(request)


@router.post("", response_model=Content[ItemCombinationMap])
async def create_one(entity: ItemCombinationMapCreateBody) -> Content[ItemCombinationMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await item_combination_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[ItemCombinationMap])
async def patch_one_by_id(id: UUID, entity: ItemCombinationMapPatchBody) -> Content[ItemCombinationMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await item_combination_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[ItemCombinationMap])
async def delete_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_combination_map_management.delete_one_by_id(request)
