from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.location import Location
from app.inners.models.value_objects.contracts.requests.managements.locations.create_body import \
    CreateBody
from app.inners.models.value_objects.contracts.requests.managements.locations.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.locations.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.locations.patch_body import \
    PatchBody
from app.inners.models.value_objects.contracts.requests.managements.locations.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.locations.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.locations.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.use_cases.managements.location_management import LocationManagement

router: APIRouter = APIRouter(tags=["locations"])


@cbv(router)
class LocationController:
    def __init__(self):
        self.location_management: LocationManagement = LocationManagement()

    @router.get("/locations")
    async def read_all(self, request: Request) -> Content[List[Location]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.location_management.read_all(request=request)

    @router.get("/locations/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Location]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.location_management.read_one_by_id(request)

    @router.post("/locations")
    async def create_one(self, body: CreateBody) -> Content[Location]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.location_management.create_one(request)

    @router.patch("/locations/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Location]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.location_management.patch_one_by_id(request)

    @router.delete("/locations/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Location]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.location_management.delete_one_by_id(request)
