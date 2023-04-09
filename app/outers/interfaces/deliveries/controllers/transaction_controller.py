from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.transaction import Transaction
from app.inners.use_cases.managements.transaction_management import TransactionManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["transactions"])


@cbv(router)
class TransactionController:
    def __init__(self):
        self.transaction_management: TransactionManagement = TransactionManagement()

    @router.get("/transactions")
    async def read_all(self) -> Content[List[Transaction]]:
        return await self.transaction_management.read_all()

    @router.get("/transactions/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Transaction]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.transaction_management.read_one_by_id(request)

    @router.post("/transactions")
    async def create_one(self, body: CreateBody) -> Content[Transaction]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.transaction_management.create_one(request)

    @router.patch("/transactions/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Transaction]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.transaction_management.patch_one_by_id(request)

    @router.delete("/transactions/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Transaction]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.transaction_management.delete_one_by_id(request)
