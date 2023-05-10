from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.use_cases.managements.transaction_item_map_management import TransactionItemMapManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transaction_item_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.read_all_request import ReadAllRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["transaction-item-maps"])


@cbv(router)
class TransactionItemMapController:
    def __init__(self):
        self.transaction_item_map_management: TransactionItemMapManagement = TransactionItemMapManagement()

    @router.get("/transaction-item-maps")
    async def read_all(self, request: Request) -> Content[List[TransactionItemMap]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.transaction_item_map_management.read_all(request=request)

    @router.get("/transaction-item-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[TransactionItemMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.transaction_item_map_management.read_one_by_id(request)

    @router.post("/transaction-item-maps")
    async def create_one(self, body: CreateBody) -> Content[TransactionItemMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.transaction_item_map_management.create_one(request)

    @router.patch("/transaction-item-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[TransactionItemMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.transaction_item_map_management.patch_one_by_id(request)

    @router.delete("/transaction-item-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[TransactionItemMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.transaction_item_map_management.delete_one_by_id(request)
