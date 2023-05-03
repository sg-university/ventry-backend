import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.item_file_map import ItemFileMap
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_file_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.item_file_map_repository import ItemFileMapRepository


class ItemFileMapManagement:
    def __init__(self):
        self.item_file_map_repository: ItemFileMapRepository = ItemFileMapRepository()

    async def read_all(self) -> Content[List[ItemFileMap]]:
        try:
            found_entities: List[ItemFileMap] = await self.item_file_map_repository.read_all()
            content: Content[List[ItemFileMap]] = Content(
                data=found_entities,
                message="ItemFileMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[ItemFileMap]] = Content(
                data=None,
                message=f"ItemFileMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[ItemFileMap]:
        try:
            found_entity: ItemFileMap = await self.item_file_map_repository.read_one_by_id(request.id)
            content: Content[ItemFileMap] = Content(
                data=found_entity,
                message="ItemFileMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemFileMap] = Content(
                data=None,
                message=f"ItemFileMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[ItemFileMap]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: ItemFileMap = ItemFileMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: ItemFileMap = await self.item_file_map_repository.create_one(entity_to_create)
            content: Content[ItemFileMap] = Content(
                data=created_entity,
                message="ItemFileMap create one succeed."
            )
        except Exception as exception:
            content: Content[ItemFileMap] = Content(
                data=None,
                message=f"ItemFileMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[ItemFileMap]:
        try:
            entity_to_patch: ItemFileMap = ItemFileMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: ItemFileMap = await self.item_file_map_repository.patch_one_by_id(request.id,
                                                                                              entity_to_patch)
            content: Content[ItemFileMap] = Content(
                data=patched_entity,
                message="ItemFileMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemFileMap] = Content(
                data=None,
                message=f"ItemFileMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[ItemFileMap]:
        try:
            deleted_entity: ItemFileMap = await self.item_file_map_repository.delete_one_by_id(request.id)
            content: Content[ItemFileMap] = Content(
                data=deleted_entity,
                message="ItemFileMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemFileMap] = Content(
                data=None,
                message=f"ItemFileMap delete one by id failed: {exception}"
            )
        return content
