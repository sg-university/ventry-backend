import uuid
from datetime import datetime
from typing import List

from app.inners.models.entities.company_account_map import CompanyAccountMap
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.company_account_map_repository import CompanyAccountMapRepository


class CompanyAccountMapManagement:
    def __init__(self):
        self.company_account_map_repository: CompanyAccountMapRepository = CompanyAccountMapRepository()

    async def read_all(self) -> Content[List[CompanyAccountMap]]:
        try:
            found_entities: List[CompanyAccountMap] = await self.company_account_map_repository.read_all()
            content: Content[List[CompanyAccountMap]] = Content(
                data=found_entities,
                message="CompanyAccountMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[CompanyAccountMap]] = Content(
                data=None,
                message=f"CompanyAccountMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[CompanyAccountMap]:
        try:
            found_entity: CompanyAccountMap = await self.company_account_map_repository.read_one_by_id(request.id)
            content: Content[CompanyAccountMap] = Content(
                data=found_entity,
                message="CompanyAccountMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyAccountMap] = Content(
                data=None,
                message=f"CompanyAccountMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[CompanyAccountMap]:
        try:
            timestamp: datetime = datetime.now()
            entity_to_create: CompanyAccountMap = CompanyAccountMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: CompanyAccountMap = await self.company_account_map_repository.create_one(entity_to_create)
            content: Content[CompanyAccountMap] = Content(
                data=created_entity,
                message="CompanyAccountMap create one succeed."
            )
        except Exception as exception:
            content: Content[CompanyAccountMap] = Content(
                data=None,
                message=f"CompanyAccountMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[CompanyAccountMap]:
        try:
            entity_to_patch: CompanyAccountMap = CompanyAccountMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(),
            )
            patched_entity: CompanyAccountMap = await self.company_account_map_repository.patch_one_by_id(request.id,
                                                                                              entity_to_patch)
            content: Content[CompanyAccountMap] = Content(
                data=patched_entity,
                message="CompanyAccountMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyAccountMap] = Content(
                data=None,
                message=f"CompanyAccountMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[CompanyAccountMap]:
        try:
            deleted_entity: CompanyAccountMap = await self.company_account_map_repository.delete_one_by_id(request.id)
            content: Content[CompanyAccountMap] = Content(
                data=deleted_entity,
                message="CompanyAccountMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyAccountMap] = Content(
                data=None,
                message=f"CompanyAccountMap delete one by id failed: {exception}"
            )
        return content
