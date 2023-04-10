from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.inners.models.entities.company_location_map import CompanyLocationMap
from app.inners.use_cases.managements.company_location_map_management import CompanyLocationMapManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["company-location-maps"])


@cbv(router)
class CompanyLocationMapController:
    def __init__(self):
        self.company_location_map_management: CompanyLocationMapManagement = CompanyLocationMapManagement()

    @router.get("/company-location-maps")
    async def read_all(self) -> Content[List[CompanyLocationMap]]:
        return await self.company_location_map_management.read_all()

    @router.get("/company-location-maps/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[CompanyLocationMap]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.company_location_map_management.read_one_by_id(request)

    @router.post("/company-location-maps")
    async def create_one(self, body: CreateBody) -> Content[CompanyLocationMap]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.company_location_map_management.create_one(request)

    @router.patch("/company-location-maps/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[CompanyLocationMap]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.company_location_map_management.patch_one_by_id(request)

    @router.delete("/company-location-maps/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[CompanyLocationMap]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.company_location_map_management.delete_one_by_id(request)
