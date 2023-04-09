import uuid
from datetime import datetime
from typing import List

from app.inners.models.entities.item_combination_map import ItemCombinationMap
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.item_combination_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.item_combination_map_repository import ItemCombinationMapRepository


class ItemCombinationMapManagement:
    def __init__(self):
        self.item_combination_map_repository: ItemCombinationMapRepository = ItemCombinationMapRepository()

    async def read_all(self) -> Content[List[ItemCombinationMap]]:
        try:
            found_entities: List[ItemCombinationMap] = await self.item_combination_map_repository.read_all()
            content: Content[List[ItemCombinationMap]] = Content(
                data=found_entities,
                message="ItemCombinationMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[ItemCombinationMap]] = Content(
                data=None,
                message=f"ItemCombinationMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[ItemCombinationMap]:
        try:
            found_entity: ItemCombinationMap = await self.item_combination_map_repository.read_one_by_id(request.id)
            content: Content[ItemCombinationMap] = Content(
                data=found_entity,
                message="ItemCombinationMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemCombinationMap] = Content(
                data=None,
                message=f"ItemCombinationMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[ItemCombinationMap]:
        try:
            timestamp: datetime = datetime.now()
            entity_to_create: ItemCombinationMap = ItemCombinationMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: ItemCombinationMap = await self.item_combination_map_repository.create_one(entity_to_create)
            content: Content[ItemCombinationMap] = Content(
                data=created_entity,
                message="ItemCombinationMap create one succeed."
            )
        except Exception as exception:
            content: Content[ItemCombinationMap] = Content(
                data=None,
                message=f"ItemCombinationMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[ItemCombinationMap]:
        try:
            entity_to_patch: ItemCombinationMap = ItemCombinationMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(),
            )
            patched_entity: ItemCombinationMap = await self.item_combination_map_repository.patch_one_by_id(request.id,
                                                                                                            entity_to_patch)
            content: Content[ItemCombinationMap] = Content(
                data=patched_entity,
                message="ItemCombinationMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemCombinationMap] = Content(
                data=None,
                message=f"ItemCombinationMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[ItemCombinationMap]:
        try:
            deleted_entity: ItemCombinationMap = await self.item_combination_map_repository.delete_one_by_id(request.id)
            content: Content[ItemCombinationMap] = Content(
                data=deleted_entity,
                message="ItemCombinationMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemCombinationMap] = Content(
                data=None,
                message=f"ItemCombinationMap delete one by id failed: {exception}"
            )
        return content
