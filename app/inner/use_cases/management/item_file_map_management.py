import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.item_file_map import ItemFileMap
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_file_map_repository


async def read_all() -> Content[List[ItemFileMap]]:
    try:
        found_entities: List[ItemFileMap] = await item_file_map_repository.read_all()
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


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[ItemFileMap]:
    try:
        found_entity: ItemFileMap = await item_file_map_repository.read_one_by_id(request.id)
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


async def create_one(request: CreateOneRequest) -> Content[ItemFileMap]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: ItemFileMap = ItemFileMap(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: ItemFileMap = await item_file_map_repository.create_one(entity_to_create)
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


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[ItemFileMap]:
    try:
        entity_to_patch: ItemFileMap = ItemFileMap(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: ItemFileMap = await item_file_map_repository.patch_one_by_id(request.id, entity_to_patch)
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


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[ItemFileMap]:
    try:
        deleted_entity: ItemFileMap = await item_file_map_repository.delete_one_by_id(request.id)
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
