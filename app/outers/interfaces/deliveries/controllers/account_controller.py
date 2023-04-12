from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.account import Account
from app.inners.use_cases.managements.account_management import AccountManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.read_all_by_company_id_request import \
    ReadAllByCompanyIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["accounts"])


@cbv(router)
class AccountController:
    def __init__(self):
        self.account_management: AccountManagement = AccountManagement()

    @router.get("/accounts")
    async def read_all(self) -> Content[List[Account]]:
        return await self.account_management.read_all()

    @router.get("/accounts/companies/{company_id}")
    async def read_one_by_company_id(self, company_id: UUID) -> Content[List[Account]]:
        request: ReadAllByCompanyIdRequest = ReadAllByCompanyIdRequest(company_id=company_id)
        return await self.account_management.read_all_by_company_id(request)

    @router.get("/accounts/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Account]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.account_management.read_one_by_id(request)

    @router.post("/accounts")
    async def create_one(self, body: CreateBody) -> Content[Account]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.account_management.create_one(request)

    @router.patch("/accounts/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Account]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.account_management.patch_one_by_id(request)

    @router.delete("/accounts/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Account]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.account_management.delete_one_by_id(request)
