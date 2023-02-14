from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.item_file_map import ItemFileMap
from app.inner.use_cases.management import item_file_map_management
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_create import \
    ItemFileMapCreate
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.item_file_map_patch import \
    ItemFileMapPatch
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/item-file-maps", tags=["item-file-maps"])


@router.get("", response_model=Content[List[ItemFileMap]])
async def read_all() -> Content[List[ItemFileMap]]:
    return await item_file_map_management.read_all()


@router.get("/{id}", response_model=Content[ItemFileMap])
async def read_one_by_id(id: UUID) -> Content[ItemFileMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_file_map_management.read_one_by_id(request)


@router.post("", response_model=Content[ItemFileMap])
async def create_one(entity: ItemFileMapCreate) -> Content[ItemFileMap]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await item_file_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[ItemFileMap])
async def patch_one_by_id(id: UUID, entity: ItemFileMapPatch) -> Content[ItemFileMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await item_file_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[ItemFileMap])
async def delete_one_by_id(id: UUID) -> Content[ItemFileMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_file_map_management.delete_one_by_id(request)
