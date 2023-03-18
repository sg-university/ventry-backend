import uuid
from datetime import datetime
from typing import List

from app.inners.models.entities.role import Role
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.roles.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories import role_repository


async def read_all() -> Content[List[Role]]:
    try:
        found_entities: List[Role] = await role_repository.read_all()
        content: Content[List[Role]] = Content(
            data=found_entities,
            message="Role read all succeed."
        )
    except Exception as exception:
        content: Content[List[Role]] = Content(
            data=None,
            message=f"Role read all failed: {exception}"
        )
    return content


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[Role]:
    try:
        found_entity: Role = await role_repository.read_one_by_id(request.id)
        content: Content[Role] = Content(
            data=found_entity,
            message="Role read one by id succeed."
        )
    except Exception as exception:
        content: Content[Role] = Content(
            data=None,
            message=f"Role read one by id failed: {exception}"
        )
    return content


async def create_one(request: CreateOneRequest) -> Content[Role]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: Role = Role(
            **request.body.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: Role = await role_repository.create_one(entity_to_create)
        content: Content[Role] = Content(
            data=created_entity,
            message="Role create one succeed."
        )
    except Exception as exception:
        content: Content[Role] = Content(
            data=None,
            message=f"Role create one failed: {exception}"
        )
    return content


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Role]:
    try:
        entity_to_patch: Role = Role(
            **request.body.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: Role = await role_repository.patch_one_by_id(request.id, entity_to_patch)
        content: Content[Role] = Content(
            data=patched_entity,
            message="Role patch one by id succeed."
        )
    except Exception as exception:
        content: Content[Role] = Content(
            data=None,
            message=f"Role patch one by id failed: {exception}"
        )
    return content


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Role]:
    try:
        deleted_entity: Role = await role_repository.delete_one_by_id(request.id)
        content: Content[Role] = Content(
            data=deleted_entity,
            message="Role delete one by id succeed."
        )
    except Exception as exception:
        content: Content[Role] = Content(
            data=None,
            message=f"Role delete one by id failed: {exception}"
        )
    return content