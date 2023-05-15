import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.item_bundle_map import ItemBundleMap
from app.inners.models.value_objects.contracts.requests.managements.item_bundle_maps.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.item_bundle_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.item_bundle_maps.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.item_bundle_maps.read_all_request import \
    ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.item_bundle_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.item_bundle_map_repository import ItemBundleMapRepository
from app.outers.utilities.management_utility import ManagementUtility


class ItemBundleMapManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.item_bundle_map_repository: ItemBundleMapRepository = ItemBundleMapRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[ItemBundleMap]]:
        try:
            found_entities: List[ItemBundleMap] = await self.item_bundle_map_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                found_entities = list(
                    filter(
                        lambda entity: self.management_utility.filter(request.query_parameter, entity),
                        found_entities
                    )
                )
            content: Content[List[ItemBundleMap]] = Content(
                data=found_entities,
                message="ItemBundleMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[ItemBundleMap]] = Content(
                data=None,
                message=f"ItemBundleMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[ItemBundleMap]:
        try:
            found_entity: ItemBundleMap = await self.item_bundle_map_repository.read_one_by_id(request.id)
            content: Content[ItemBundleMap] = Content(
                data=found_entity,
                message="ItemBundleMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemBundleMap] = Content(
                data=None,
                message=f"ItemBundleMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[ItemBundleMap]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: ItemBundleMap = ItemBundleMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: ItemBundleMap = await self.item_bundle_map_repository.create_one(entity_to_create)
            content: Content[ItemBundleMap] = Content(
                data=created_entity,
                message="ItemBundleMap create one succeed."
            )
        except Exception as exception:
            content: Content[ItemBundleMap] = Content(
                data=None,
                message=f"ItemBundleMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[ItemBundleMap]:
        try:
            entity_to_patch: ItemBundleMap = ItemBundleMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: ItemBundleMap = await self.item_bundle_map_repository.patch_one_by_id(request.id,
                                                                                                  entity_to_patch)
            content: Content[ItemBundleMap] = Content(
                data=patched_entity,
                message="ItemBundleMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemBundleMap] = Content(
                data=None,
                message=f"ItemBundleMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[ItemBundleMap]:
        try:
            deleted_entity: ItemBundleMap = await self.item_bundle_map_repository.delete_one_by_id(request.id)
            content: Content[ItemBundleMap] = Content(
                data=deleted_entity,
                message="ItemBundleMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[ItemBundleMap] = Content(
                data=None,
                message=f"ItemBundleMap delete one by id failed: {exception}"
            )
        return content
