from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.item_bundle_map import ItemBundleMap
from app.inners.use_cases.managements.item_bundle_map_management import ItemBundleMapManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_bundle_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["item-bundle-maps"])


@cbv(router)
class ItemBundleMapController:
    def __init__(self):
        self.item_bundle_map_management: ItemBundleMapManagement = ItemBundleMapManagement()

    @router.get("/item-bundle-maps")
    async def read_all(self) -> Content[List[ItemBundleMap]]:
        return await self.item_bundle_map_management.read_all()

    @router.get("/item-bundle-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[ItemBundleMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.item_bundle_map_management.read_one_by_id(request)

    @router.post("/item-bundle-maps")
    async def create_one(self, body: CreateBody) -> Content[ItemBundleMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.item_bundle_map_management.create_one(request)

    @router.patch("/item-bundle-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[ItemBundleMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.item_bundle_map_management.patch_one_by_id(request)

    @router.delete("/item-bundle-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[ItemBundleMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.item_bundle_map_management.delete_one_by_id(request)
