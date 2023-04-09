from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.use_cases.managements.inventory_control_management import InventoryControlManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["inventory-controls"])


@cbv(router)
class InventoryControlController:
    def __init__(self):
        self.inventory_control_management: InventoryControlManagement = InventoryControlManagement()

    @router.get("/inventory-controls")
    async def read_all(self) -> Content[List[InventoryControl]]:
        return await self.inventory_control_management.read_all()

    @router.get("/inventory-controls/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[InventoryControl]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.inventory_control_management.read_one_by_id(request)

    @router.post("/inventory-controls")
    async def create_one(self, body: CreateBody) -> Content[InventoryControl]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.inventory_control_management.create_one(request)

    @router.patch("/inventory-controls/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[InventoryControl]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.inventory_control_management.patch_one_by_id(request)

    @router.delete("/inventory-controls/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[InventoryControl]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.inventory_control_management.delete_one_by_id(request)
