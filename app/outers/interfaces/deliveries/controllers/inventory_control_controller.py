from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.use_cases.managements import inventory_control_management
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(prefix="/inventory-controls", tags=["inventory-controls"])


@router.get("", response_model=Content[List[InventoryControl]])
async def read_all() -> Content[List[InventoryControl]]:
    return await inventory_control_management.read_all()


@router.get("/{id}", response_model=Content[InventoryControl])
async def read_one_by_id(id: UUID) -> Content[InventoryControl]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return await inventory_control_management.read_one_by_id(request)


@router.post("", response_model=Content[InventoryControl])
async def create_one(body: CreateBody) -> Content[InventoryControl]:
    request: CreateOneRequest = CreateOneRequest(body=body)
    return await inventory_control_management.create_one(request)


@router.patch("/{id}", response_model=Content[InventoryControl])
async def patch_one_by_id(id: UUID, body: PatchBody) -> Content[InventoryControl]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
    return await inventory_control_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[InventoryControl])
async def delete_one_by_id(id: UUID) -> Content[InventoryControl]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return await inventory_control_management.delete_one_by_id(request)
