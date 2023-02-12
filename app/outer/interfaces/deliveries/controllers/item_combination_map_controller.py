from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.item_combination_map import ItemCombinationMap
from app.inner.use_cases.management import item_combination_map_management
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_create import \
    ItemCombinationMapCreate
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.item_combination_map_patch import \
    ItemCombinationMapPatch
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/item-combination-maps", tags=["item-combination-maps"])


@router.get("", response_model=Content[List[ItemCombinationMap]])
def read_all() -> Content[List[ItemCombinationMap]]:
    return item_combination_map_management.read_all()


@router.get("/{id}", response_model=Content[ItemCombinationMap])
def read_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return item_combination_map_management.read_one_by_id(request)


@router.post("", response_model=Content[ItemCombinationMap])
def create_one(entity: ItemCombinationMapCreate) -> Content[ItemCombinationMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return item_combination_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[ItemCombinationMap])
def patch_one_by_id(id: UUID, entity: ItemCombinationMapPatch) -> Content[ItemCombinationMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return item_combination_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[ItemCombinationMap])
def delete_one_by_id(id: UUID) -> Content[ItemCombinationMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return item_combination_map_management.delete_one_by_id(request)
