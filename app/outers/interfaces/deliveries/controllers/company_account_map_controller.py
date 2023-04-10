from typing import List
from uuid import UUID

from app.inners.use_cases.managements.company_account_map_management import CompanyAccountMapManagement
from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.company_account_map import CompanyAccountMap
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["company-account-maps"])


@cbv(router)
class CompanyAccountMapController:
    def __init__(self):
        self.company_account_map_management: CompanyAccountMapManagement = CompanyAccountMapManagement()

    @router.get("/company-account-maps")
    async def read_all(self) -> Content[List[CompanyAccountMap]]:
        return await self.company_account_map_management.read_all()

    @router.get("/company-account-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[CompanyAccountMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.company_account_map_management.read_one_by_id(request)

    @router.post("/company-account-maps")
    async def create_one(self, body: CreateBody) -> Content[CompanyAccountMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.company_account_map_management.create_one(request)

    @router.patch("/company-account-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[CompanyAccountMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.company_account_map_management.patch_one_by_id(request)

    @router.delete("/company-account-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[CompanyAccountMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.company_account_map_management.delete_one_by_id(request)
