import uuid
from datetime import datetime
from typing import List

from app.outers.repositories.company_location_map_repository import CompanyLocationMapRepository

from app.inners.models.entities.company_location_map import CompanyLocationMap
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.company_location_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content


class CompanyLocationMapManagement:
    def __init__(self):
        self.company_location_map_repository: CompanyLocationMapRepository = CompanyLocationMapRepository()

    async def read_all(self) -> Content[List[CompanyLocationMap]]:
        try:
            found_entities: List[CompanyLocationMap] = await self.company_location_map_repository.read_all()
            content: Content[List[CompanyLocationMap]] = Content(
                data=found_entities,
                message="CompanyLocationMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[CompanyLocationMap]] = Content(
                data=None,
                message=f"CompanyLocationMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[CompanyLocationMap]:
        try:
            found_entity: CompanyLocationMap = await self.company_location_map_repository.read_one_by_id(request.id)
            content: Content[CompanyLocationMap] = Content(
                data=found_entity,
                message="CompanyLocationMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyLocationMap] = Content(
                data=None,
                message=f"CompanyLocationMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[CompanyLocationMap]:
        try:
            timestamp: datetime = datetime.now()
            entity_to_create: CompanyLocationMap = CompanyLocationMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: CompanyLocationMap = await self.company_location_map_repository.create_one(entity_to_create)
            content: Content[CompanyLocationMap] = Content(
                data=created_entity,
                message="CompanyLocationMap create one succeed."
            )
        except Exception as exception:
            content: Content[CompanyLocationMap] = Content(
                data=None,
                message=f"CompanyLocationMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[CompanyLocationMap]:
        try:
            entity_to_patch: CompanyLocationMap = CompanyLocationMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(),
            )
            patched_entity: CompanyLocationMap = await self.company_location_map_repository.patch_one_by_id(request.id,
                                                                                                            entity_to_patch)
            content: Content[CompanyLocationMap] = Content(
                data=patched_entity,
                message="CompanyLocationMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyLocationMap] = Content(
                data=None,
                message=f"CompanyLocationMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[CompanyLocationMap]:
        try:
            deleted_entity: CompanyLocationMap = await self.company_location_map_repository.delete_one_by_id(request.id)
            content: Content[CompanyLocationMap] = Content(
                data=deleted_entity,
                message="CompanyLocationMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[CompanyLocationMap] = Content(
                data=None,
                message=f"CompanyLocationMap delete one by id failed: {exception}"
            )
        return content
