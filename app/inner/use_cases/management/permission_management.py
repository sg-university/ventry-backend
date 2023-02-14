import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.permission import Permission
from app.outer.interfaces.deliveries.contracts.requests.permission_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.permission_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.permission_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.permission_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import permission_repository


async def read_all() -> Content[List[Permission]]:
    try:
        found_entities: List[Permission] = await permission_repository.read_all()
        content: Content[List[Permission]] = Content(
            data=found_entities,
            message="Permission read all succeed."
        )
    except Exception as exception:
        content: Content[List[Permission]] = Content(
            data=None,
            message=f"Permission read all failed: {exception}"
        )
    return content


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[Permission]:
    try:
        found_entity: Permission = await permission_repository.read_one_by_id(request.id)
        content: Content[Permission] = Content(
            data=found_entity,
            message="Permission read one by id succeed."
        )
    except Exception as exception:
        content: Content[Permission] = Content(
            data=None,
            message=f"Permission read one by id failed: {exception}"
        )
    return content


async def create_one(request: CreateOneRequest) -> Content[Permission]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: Permission = Permission(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: Permission = await permission_repository.create_one(entity_to_create)
        content: Content[Permission] = Content(
            data=created_entity,
            message="Permission create one succeed."
        )
    except Exception as exception:
        content: Content[Permission] = Content(
            data=None,
            message=f"Permission create one failed: {exception}"
        )
    return content


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Permission]:
    try:
        entity_to_patch: Permission = Permission(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: Permission = await permission_repository.patch_one_by_id(request.id, entity_to_patch)
        content: Content[Permission] = Content(
            data=patched_entity,
            message="Permission patch one by id succeed."
        )
    except Exception as exception:
        content: Content[Permission] = Content(
            data=None,
            message=f"Permission patch one by id failed: {exception}"
        )
    return content


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Permission]:
    try:
        deleted_entity: Permission = await permission_repository.delete_one_by_id(request.id)
        content: Content[Permission] = Content(
            data=deleted_entity,
            message="Permission delete one by id succeed."
        )
    except Exception as exception:
        content: Content[Permission] = Content(
            data=None,
            message=f"Permission delete one by id failed: {exception}"
        )
    return content
