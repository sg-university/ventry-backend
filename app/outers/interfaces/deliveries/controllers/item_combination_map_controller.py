from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.item_combination_map import ItemCombinationMap
from app.inners.use_cases.managements.item_combination_map_management import ItemCombinationMapManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["item-combination-maps"])


@cbv(router)
class ItemCombinationMapController:
    def __init__(self):
        self.item_combination_map_management: ItemCombinationMapManagement = ItemCombinationMapManagement()

    @router.get("/item-combination-maps")
    async def read_all(self) -> Content[List[ItemCombinationMap]]:
        return await self.item_combination_map_management.read_all()

    @router.get("/item-combination-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[ItemCombinationMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.item_combination_map_management.read_one_by_id(request)

    @router.post("/item-combination-maps")
    async def create_one(self, body: CreateBody) -> Content[ItemCombinationMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.item_combination_map_management.create_one(request)

    @router.patch("/item-combination-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[ItemCombinationMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.item_combination_map_management.patch_one_by_id(request)

    @router.delete("/item-combination-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[ItemCombinationMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.item_combination_map_management.delete_one_by_id(request)
