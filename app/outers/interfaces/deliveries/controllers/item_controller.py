from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.item import Item
from app.inners.use_cases.managements import item_management
from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.items.patch_body import PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.items.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=Content[List[Item]])
async def read_all() -> Content[List[Item]]:
    return await item_management.read_all()


@router.get("/{id}", response_model=Content[Item])
async def read_one_by_id(id: UUID) -> Content[Item]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await item_management.read_one_by_id(request)


@router.post("", response_model=Content[Item])
async def create_one(body: CreateBody) -> Content[Item]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await item_management.create_one(request)


@router.patch("/{id}", response_model=Content[Item])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[Item]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await item_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[Item])
async def delete_one_by_id(id: UUID) -> Content[Item]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await item_management.delete_one_by_id(request)
