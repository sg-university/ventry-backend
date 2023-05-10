from typing import List
from uuid import UUID

from fastapi import APIRouter, Request
from fastapi_utils.cbv import cbv

from app.inners.models.entities.role import Role
from app.inners.use_cases.managements.role_management import RoleManagement
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.create_body import \
    CreateBody
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_body import \
    PatchBody
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.read_all_request import ReadAllRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content

router: APIRouter = APIRouter(tags=["roles"])


@cbv(router)
class RoleController:
    def __init__(self):
        self.role_management: RoleManagement = RoleManagement()

    @router.get("/roles")
    async def read_all(self, request: Request) -> Content[List[Role]]:
        request: ReadAllRequest = ReadAllRequest(query_parameter=dict(request.query_params))
        return await self.role_management.read_all(request=request)

    @router.get("/roles/{id}")
    async def read_one_by_id(self, id: UUID) -> Content[Role]:
        request: ReadOneByIdRequest = ReadOneByIdRequest(id=id)
        return await self.role_management.read_one_by_id(request)

    @router.post("/roles")
    async def create_one(self, body: CreateBody) -> Content[Role]:
        request: CreateOneRequest = CreateOneRequest(body=body)
        return await self.role_management.create_one(request)

    @router.patch("/roles/{id}")
    async def patch_one_by_id(self, id: UUID, body: PatchBody) -> Content[Role]:
        request: PatchOneByIdRequest = PatchOneByIdRequest(id=id, body=body)
        return await self.role_management.patch_one_by_id(request)

    @router.delete("/roles/{id}")
    async def delete_one_by_id(self, id: UUID) -> Content[Role]:
        request: DeleteOneByIdRequest = DeleteOneByIdRequest(id=id)
        return await self.role_management.delete_one_by_id(request)
