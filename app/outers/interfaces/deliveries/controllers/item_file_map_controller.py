from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.item_file_map import ItemFileMap
from app.inners.use_cases.managements.item_file_map_management import ItemFileMapManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["item-file-maps"])


@cbv(router)
class ItemFileMapController:
    def __init__(self):
        self.item_file_map_management: ItemFileMapManagement = ItemFileMapManagement()

    @router.get("/item-file-maps")
    async def read_all(self) -> Content[List[ItemFileMap]]:
        return await self.item_file_map_management.read_all()

    @router.get("/item-file-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[ItemFileMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.item_file_map_management.read_one_by_id(request)

    @router.post("/item-file-maps")
    async def create_one(self, body: CreateBody) -> Content[ItemFileMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.item_file_map_management.create_one(request)

    @router.patch("/item-file-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[ItemFileMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.item_file_map_management.patch_one_by_id(request)

    @router.delete("/item-file-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[ItemFileMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.item_file_map_management.delete_one_by_id(request)
