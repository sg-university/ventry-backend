from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.item import Item
from app.inners.use_cases.managements.item_management import ItemManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.items.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["items"])


@cbv(router)
class ItemController:
    def __init__(self):
        self.item_management: ItemManagement = ItemManagement()

    @router.get("/items")
    async def read_all(self) -> Content[List[Item]]:
        return await self.item_management.read_all()

    @router.get("/items/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Item]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.item_management.read_one_by_id(request)

    @router.post("/items")
    async def create_one(self, body: CreateBody) -> Content[Item]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.item_management.create_one(request)

    @router.patch("/items/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Item]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.item_management.patch_one_by_id(request)

    @router.delete("/items/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Item]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.item_management.delete_one_by_id(request)
