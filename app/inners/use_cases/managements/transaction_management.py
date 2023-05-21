import asyncio
import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.entities.item import Item
from app.inners.models.entities.transaction import Transaction
from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_request import CheckoutRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.transactions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.managements.transactions.checkout_response import CheckoutResponse
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.inventory_control_repository import InventoryControlRepository
from app.outers.repositories.item_repository import ItemRepository
from app.outers.repositories.transaction_item_map_repository import TransactionItemMapRepository
from app.outers.repositories.transaction_repository import TransactionRepository
from app.outers.utilities.management_utility import ManagementUtility
from test.utilities import locker


class TransactionManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.transaction_repository: TransactionRepository = TransactionRepository()
        self.transaction_item_map_repository: TransactionItemMapRepository = TransactionItemMapRepository()
        self.inventory_control_repository: InventoryControlRepository = InventoryControlRepository()
        self.item_repository: ItemRepository = ItemRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[Transaction]]:
        try:
            found_entities: List[Transaction] = await self.transaction_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "location_id" in request.query_parameter.keys():
                    found_entities = await self.transaction_repository.read_all_by_location_id(
                        location_id=uuid.UUID(request.query_parameter["location_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[Transaction]] = Content(
                data=found_entities,
                message="Transaction read all succeed."
            )
        except Exception as exception:
            content: Content[List[Transaction]] = Content(
                data=None,
                message=f"Transaction read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[Transaction]:
        try:
            found_entity: Transaction = await self.transaction_repository.read_one_by_id(request.id)
            content: Content[Transaction] = Content(
                data=found_entity,
                message="Transaction read one by id succeed."
            )
        except Exception as exception:
            content: Content[Transaction] = Content(
                data=None,
                message=f"Transaction read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[Transaction]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: Transaction = Transaction(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: Transaction = await self.transaction_repository.create_one(entity_to_create)
            content: Content[Transaction] = Content(
                data=created_entity,
                message="Transaction create one succeed."
            )
        except Exception as exception:
            content: Content[Transaction] = Content(
                data=None,
                message=f"Transaction create one failed: {exception}"
            )
        return content

    @locker.wait_lock
    async def checkout(self, request: CheckoutRequest) -> Content[CheckoutResponse]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)

            created_transaction: Transaction = await self.transaction_repository.create_one(
                Transaction(
                    **request.body.transaction.dict(),
                    id=uuid.uuid4(),
                    created_at=timestamp,
                    updated_at=timestamp,
                )
            )

            transaction_item_map_coroutines = []
            inventory_control_coroutines = []
            for transaction_item_map in request.body.transaction_item_maps:
                transaction_item_map_coroutine = self.transaction_item_map_repository.create_one(
                    TransactionItemMap(
                        **transaction_item_map.dict(),
                        id=uuid.uuid4(),
                        transaction_id=created_transaction.id,
                        created_at=timestamp,
                        updated_at=timestamp,
                    )
                )
                transaction_item_map_coroutines.append(transaction_item_map_coroutine)

                if request.body.is_record_to_inventory_controls:
                    item: Item = await self.item_repository.read_one_by_id(transaction_item_map.item_id)

                    inventory_control_coroutine = self.inventory_control_repository.create_one(
                        InventoryControl(
                            id=uuid.uuid4(),
                            account_id=request.body.transaction.account_id,
                            item_id=item.id,
                            quantity_before=item.quantity,
                            quantity_after=item.quantity - transaction_item_map.quantity,
                            timestamp=request.body.transaction.timestamp,
                            created_at=timestamp,
                            updated_at=timestamp,
                        )
                    )
                    inventory_control_coroutines.append(inventory_control_coroutine)

            created_transaction_item_maps: List[TransactionItemMap] = await asyncio.gather(
                *transaction_item_map_coroutines
            )
            created_inventory_controls: List[InventoryControl] = await asyncio.gather(
                *inventory_control_coroutines
            )

            content: Content[CheckoutResponse] = Content(
                data=CheckoutResponse(
                    transaction=created_transaction,
                    transaction_item_maps=created_transaction_item_maps,
                    inventory_controls=created_inventory_controls,
                ),
                message="Checkout succeed."
            )
        except Exception as exception:
            content: Content[CheckoutResponse] = Content(
                data=None,
                message=f"Checkout failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[Transaction]:
        try:
            entity_to_patch: Transaction = Transaction(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: Transaction = await self.transaction_repository.patch_one_by_id(request.id,
                                                                                            entity_to_patch)
            content: Content[Transaction] = Content(
                data=patched_entity,
                message="Transaction patch one by id succeed."
            )
        except Exception as exception:
            content: Content[Transaction] = Content(
                data=None,
                message=f"Transaction patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[Transaction]:
        try:
            deleted_entity: Transaction = await self.transaction_repository.delete_one_by_id(request.id)
            content: Content[Transaction] = Content(
                data=deleted_entity,
                message="Transaction delete one by id succeed."
            )
        except Exception as exception:
            content: Content[Transaction] = Content(
                data=None,
                message=f"Transaction delete one by id failed: {exception}"
            )
        return content
