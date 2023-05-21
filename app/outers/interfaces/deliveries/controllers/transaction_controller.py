from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.transaction import Transaction
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_body import CheckoutBody
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_request import CheckoutRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.create_body import \
    CreateBody
from app.inners.models.value_objects.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.patch_body import \
    PatchBody
from app.inners.models.value_objects.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.read_all_request import \
    ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.managements.transactions.checkout_response import CheckoutResponse
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.transaction_management import TransactionManagement

router: APIRouter = APIRouter(tags=["transactions"])


@cbv(router)
class TransactionController:
    def __init__(self):
        self.transaction_management: TransactionManagement = TransactionManagement()

    @router.get("/transactions")
    async def read_all(self, request: Request) -> Content[List[Transaction]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.transaction_management.read_all(request=request)

    @router.get("/transactions/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Transaction]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.transaction_management.read_one_by_id(request)

    @router.post("/transactions")
    async def create_one(self, body: CreateBody) -> Content[Transaction]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.transaction_management.create_one(request)

    @router.post("/transactions/checkout")
    async def checkout(self, body: CheckoutBody) -> Content[CheckoutResponse]:
        request: CheckoutRequest = CheckoutRequest(body=body)
        return await self.transaction_management.checkout(request)

    @router.patch("/transactions/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Transaction]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.transaction_management.patch_one_by_id(request)

    @router.delete("/transactions/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Transaction]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.transaction_management.delete_one_by_id(request)
