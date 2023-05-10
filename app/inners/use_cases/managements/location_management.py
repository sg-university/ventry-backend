import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.location import Location
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.read_all_request import ReadAllRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.locations.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.location_repository import LocationRepository
from app.outers.utilities.management_utility import ManagementUtility


class LocationManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.location_repository: LocationRepository = LocationRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[Location]]:
        try:
            found_entities: List[Location] = await self.location_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "account_id" in request.query_parameter.keys():
                    found_entities = await self.location_repository.read_all_by_account_id(
                        account_id=uuid.UUID(request.query_parameter["account_id"])
                    )
                elif "item_id" in request.query_parameter.keys():
                    found_entities = await self.location_repository.read_all_by_item_id(
                        item_id=uuid.UUID(request.query_parameter["item_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[Location]] = Content(
                data=found_entities,
                message="Location read all succeed."
            )
        except Exception as exception:
            content: Content[List[Location]] = Content(
                data=None,
                message=f"Location read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[Location]:
        try:
            found_entity: Location = await self.location_repository.read_one_by_id(request.id)
            content: Content[Location] = Content(
                data=found_entity,
                message="Location read one by id succeed."
            )
        except Exception as exception:
            content: Content[Location] = Content(
                data=None,
                message=f"Location read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[Location]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: Location = Location(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: Location = await self.location_repository.create_one(entity_to_create)
            content: Content[Location] = Content(
                data=created_entity,
                message="Location create one succeed."
            )
        except Exception as exception:
            content: Content[Location] = Content(
                data=None,
                message=f"Location create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[Location]:
        try:
            entity_to_patch: Location = Location(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: Location = await self.location_repository.patch_one_by_id(request.id, entity_to_patch)
            content: Content[Location] = Content(
                data=patched_entity,
                message="Location patch one by id succeed."
            )
        except Exception as exception:
            content: Content[Location] = Content(
                data=None,
                message=f"Location patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[Location]:
        try:
            deleted_entity: Location = await self.location_repository.delete_one_by_id(request.id)
            content: Content[Location] = Content(
                data=deleted_entity,
                message="Location delete one by id succeed."
            )
        except Exception as exception:
            content: Content[Location] = Content(
                data=None,
                message=f"Location delete one by id failed: {exception}"
            )
        return content
