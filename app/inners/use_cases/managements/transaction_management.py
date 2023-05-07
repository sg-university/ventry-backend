import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.transaction import Transaction
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.transactions.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.transaction_repository import TransactionRepository


class TransactionManagement:
    def __init__(self):
        self.transaction_repository: TransactionRepository = TransactionRepository()

    async def read_all(self) -> Content[List[Transaction]]:
        try:
            found_entities: List[Transaction] = await self.transaction_repository.read_all()
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
