import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.transaction_item_map import TransactionItemMap
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import transaction_item_map_repository


async def read_all() -> Content[List[TransactionItemMap]]:
    try:
        found_entities: List[TransactionItemMap] = await transaction_item_map_repository.read_all()
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


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[TransactionItemMap]:
    try:
        found_entity: TransactionItemMap = await transaction_item_map_repository.read_one_by_id(request.id)
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


async def create_one(request: CreateOneRequest) -> Content[TransactionItemMap]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: TransactionItemMap = TransactionItemMap(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: TransactionItemMap = await transaction_item_map_repository.create_one(entity_to_create)
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


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[TransactionItemMap]:
    try:
        entity_to_patch: TransactionItemMap = TransactionItemMap(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: TransactionItemMap = await transaction_item_map_repository.patch_one_by_id(request.id,
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


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[TransactionItemMap]:
    try:
        deleted_entity: TransactionItemMap = await transaction_item_map_repository.delete_one_by_id(request.id)
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
