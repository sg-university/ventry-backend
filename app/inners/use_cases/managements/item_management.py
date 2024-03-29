import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.item import Item
from app.inners.models.value_objects.contracts.requests.managements.items.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.items.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.items.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.items.read_all_request import \
    ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.items.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.item_repository import ItemRepository
from app.outers.utilities.management_utility import ManagementUtility


class ItemManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.item_repository: ItemRepository = ItemRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[Item]]:
        try:
            found_entities: List[Item] = await self.item_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "account_id" in request.query_parameter.keys():
                    found_entities = await self.item_repository.read_all_by_account_id(
                        account_id=uuid.UUID(request.query_parameter["account_id"])
                    )
                elif "location_id" in request.query_parameter.keys():
                    found_entities = await self.item_repository.read_all_by_location_id(
                        location_id=uuid.UUID(request.query_parameter["location_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[Item]] = Content(
                data=found_entities,
                message="Item read all succeed."
            )
        except Exception as exception:
            content: Content[List[Item]] = Content(
                data=None,
                message=f"Item read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[Item]:
        try:
            found_entity: Item = await self.item_repository.read_one_by_id(request.id)
            content: Content[Item] = Content(
                data=found_entity,
                message="Item read one by id succeed."
            )
        except Exception as exception:
            content: Content[Item] = Content(
                data=None,
                message=f"Item read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[Item]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: Item = Item(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: Item = await self.item_repository.create_one(entity_to_create)
            content: Content[Item] = Content(
                data=created_entity,
                message="Item create one succeed."
            )
        except Exception as exception:
            content: Content[Item] = Content(
                data=None,
                message=f"Item create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[Item]:
        try:
            entity_to_patch: Item = Item(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: Item = await self.item_repository.patch_one_by_id(request.id,
                                                                              entity_to_patch)
            content: Content[Item] = Content(
                data=patched_entity,
                message="Item patch one by id succeed."
            )
        except Exception as exception:
            content: Content[Item] = Content(
                data=None,
                message=f"Item patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[Item]:
        try:
            deleted_entity: Item = await self.item_repository.delete_one_by_id(request.id)
            content: Content[Item] = Content(
                data=deleted_entity,
                message="Item delete one by id succeed."
            )
        except Exception as exception:
            content: Content[Item] = Content(
                data=None,
                message=f"Item delete one by id failed: {exception}"
            )
        return content
