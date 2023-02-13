from typing import List
from uuid import UUID

from fastapi import APIRouter

from app.inner.models.entities.inventory_control import InventoryControl
from app.inner.use_cases.management import inventory_control_management
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.inventory_control_create import \
    InventoryControlCreate
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.inventory_control_patch import \
    InventoryControlPatch
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content

router: APIRouter = APIRouter(prefix="/inventory-controls", tags=["inventory-controls"])


@router.get("", response_model=Content[List[InventoryControl]])
def read_all() -> Content[List[InventoryControl]]:
    return inventory_control_management.read_all()


@router.get("/{id}", response_model=Content[InventoryControl])
def read_one_by_id(id: UUID) -> Content[InventoryControl]:
    request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
    return inventory_control_management.read_one_by_id(request)


@router.post("", response_model=Content[InventoryControl])
def create_one(entity: InventoryControlCreate) -> Content[InventoryControl]:
    request: CreateOneRequest = CreateOneRequest(entity=entity)
    return inventory_control_management.create_one(request)


@router.patch("/{id}", response_model=Content[InventoryControl])
def patch_one_by_id(id: UUID, entity: InventoryControlPatch) -> Content[InventoryControl]:
    request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, entity=entity)
    return inventory_control_management.patch_one_by_id(request)


@router.delete("/{id}", response_model=Content[InventoryControl])
def delete_one_by_id(id: UUID) -> Content[InventoryControl]:
    request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
    return inventory_control_management.delete_one_by_id(request)
