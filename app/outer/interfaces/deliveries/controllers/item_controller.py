from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.item import Item
from app.inner.use_cases.management import item_management
from app.outer.interfaces.deliveries.contracts.requests.item_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.item_create import ItemCreate
from app.outer.interfaces.deliveries.contracts.requests.item_management.item_patch import ItemPatch
from app.outer.interfaces.deliveries.contracts.requests.item_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.read_one_by_id_request import ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=Content[List[Item]])
async def read_all() -> Content[List[Item]]:
    return await item_management.read_all()


@router.get("/{id}", response_model=Content[Item])
async def read_one_by_id(id: UUID) -> Content[Item]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_management.read_one_by_id(request)


@router.post("", response_model=Content[Item])
async def create_one(entity: ItemCreate) -> Content[Item]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return await item_management.create_one(request)


@router.patch("/{id}", response_model=Content[Item])
async def patch_one_by_id(id: UUID, entity: ItemPatch) -> Content[Item]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return await item_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Item])
async def delete_one_by_id(id: UUID) -> Content[Item]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_management.delete_one_by_id(request)
