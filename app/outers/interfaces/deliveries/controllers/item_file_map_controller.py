from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.item_file_map import ItemFileMap
from app.inners.use_cases.managements import item_file_map_management
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/item-file-maps", tags=["item-file-maps"])


@router.get("", response_model=Content[List[ItemFileMap]])
async def read_all() -> Content[List[ItemFileMap]]:
    return await item_file_map_management.read_all()


@router.get("/{id}", response_model=Content[ItemFileMap])
async def read_one_by_id(id: UUID) -> Content[ItemFileMap]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_file_map_management.read_one_by_id(request)


@router.post("", response_model=Content[ItemFileMap])
async def create_one(body: CreateBody) -> Content[ItemFileMap]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await item_file_map_management.create_one(request)


@router.patch("/{id}", response_model=Content[ItemFileMap])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[ItemFileMap]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await item_file_map_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[ItemFileMap])
async def delete_one_by_id(id: UUID) -> Content[ItemFileMap]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_file_map_management.delete_one_by_id(request)
