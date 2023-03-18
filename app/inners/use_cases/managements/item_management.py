import uuid
from datetime import datetime
from typing import List

from app.inners.models.entities.item import Item
from app.outers.interfaces.deliveries.contracts.requests.managements.items.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.items.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories import item_repository


async def read_all() -> Content[List[Item]]:
    try:
        found_entities: List[Item] = await item_repository.read_all()
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


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[Item]:
    try:
        found_entity: Item = await item_repository.read_one_by_id(request.id)
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


async def create_one(request: CreateOneRequest) -> Content[Item]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: Item = Item(
            **request.body.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: Item = await item_repository.create_one(entity_to_create)
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


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Item]:
    try:
        entity_to_patch: Item = Item(
            **request.body.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: Item = await item_repository.patch_one_by_id(request.id, entity_to_patch)
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


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Item]:
    try:
        deleted_entity: Item = await item_repository.delete_one_by_id(request.id)
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
