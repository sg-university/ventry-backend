import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.transaction import Transaction
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import transaction_repository


async def read_all() -> Content[List[Transaction]]:
    try:
        found_entities: List[Transaction] = await transaction_repository.read_all()
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


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[Transaction]:
    try:
        found_entity: Transaction = await transaction_repository.read_one_by_id(request.id)
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


async def create_one(request: CreateOneRequest) -> Content[Transaction]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: Transaction = Transaction(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: Transaction = await transaction_repository.create_one(entity_to_create)
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


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Transaction]:
    try:
        entity_to_patch: Transaction = Transaction(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: Transaction = await transaction_repository.patch_one_by_id(request.id, entity_to_patch)
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


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Transaction]:
    try:
        deleted_entity: Transaction = await transaction_repository.delete_one_by_id(request.id)
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
