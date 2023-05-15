from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.company import Company
from app.inners.models.value_objects.contracts.requests.managements.companies.create_body import \
    CreateBody
from app.inners.models.value_objects.contracts.requests.managements.companies.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.patch_body import \
    PatchBody
from app.inners.models.value_objects.contracts.requests.managements.companies.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.company_management import CompanyManagement

router: APIRouter = APIRouter(tags=["companies"])


@cbv(router)
class CompanyController:
    def __init__(self):
        self.company_management: CompanyManagement = CompanyManagement()

    @router.get("/companies")
    async def read_all(self, request: Request) -> Content[List[Company]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.company_management.read_all(request=request)

    @router.get("/companies/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Company]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.company_management.read_one_by_id(request)

    @router.post("/companies")
    async def create_one(self, body: CreateBody) -> Content[Company]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.company_management.create_one(request)

    @router.patch("/companies/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Company]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.company_management.patch_one_by_id(request)

    @router.delete("/companies/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Company]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.company_management.delete_one_by_id(request)
