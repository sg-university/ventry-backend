import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.models.value_objects.contracts.requests.managements.transaction_item_maps.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transaction_item_maps.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.read_all_request import \
    ReadAllRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.transaction_item_map_repository import TransactionItemMapRepository
from app.outers.utilities.management_utility import ManagementUtility


class TransactionItemMapManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.transaction_item_map_repository: TransactionItemMapRepository = TransactionItemMapRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[TransactionItemMap]]:
        try:
            found_entities: List[TransactionItemMap] = await self.transaction_item_map_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "account_id" in request.query_parameter.keys():
                    found_entities = await self.transaction_item_map_repository.read_all_by_account_id(
                        account_id=uuid.UUID(request.query_parameter["account_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[TransactionItemMap]] = Content(
                data=found_entities,
                message="TransactionItemMap read all succeed."
            )
        except Exception as exception:
            content: Content[List[TransactionItemMap]] = Content(
                data=None,
                message=f"TransactionItemMap read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[TransactionItemMap]:
        try:
            found_entity: TransactionItemMap = await self.transaction_item_map_repository.read_one_by_id(request.id)
            content: Content[TransactionItemMap] = Content(
                data=found_entity,
                message="TransactionItemMap read one by id succeed."
            )
        except Exception as exception:
            content: Content[TransactionItemMap] = Content(
                data=None,
                message=f"TransactionItemMap read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[TransactionItemMap]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: TransactionItemMap = TransactionItemMap(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: TransactionItemMap = await self.transaction_item_map_repository.create_one(entity_to_create)
            content: Content[TransactionItemMap] = Content(
                data=created_entity,
                message="TransactionItemMap create one succeed."
            )
        except Exception as exception:
            content: Content[TransactionItemMap] = Content(
                data=None,
                message=f"TransactionItemMap create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[TransactionItemMap]:
        try:
            entity_to_patch: TransactionItemMap = TransactionItemMap(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: TransactionItemMap = await self.transaction_item_map_repository.patch_one_by_id(request.id,
                                                                                                            entity_to_patch)
            content: Content[TransactionItemMap] = Content(
                data=patched_entity,
                message="TransactionItemMap patch one by id succeed."
            )
        except Exception as exception:
            content: Content[TransactionItemMap] = Content(
                data=None,
                message=f"TransactionItemMap patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[TransactionItemMap]:
        try:
            deleted_entity: TransactionItemMap = await self.transaction_item_map_repository.delete_one_by_id(request.id)
            content: Content[TransactionItemMap] = Content(
                data=deleted_entity,
                message="TransactionItemMap delete one by id succeed."
            )
        except Exception as exception:
            content: Content[TransactionItemMap] = Content(
                data=None,
                message=f"TransactionItemMap delete one by id failed: {exception}"
            )
        return content
