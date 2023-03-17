import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.content import Content
from app.outer.repositories import account_permission_map_repository


async def read_all() -> Content[List[AccountPermissionMap]]:
    try:
        found_entities: List[AccountPermissionMap] = await account_permission_map_repository.read_all()
        content: Content[List[AccountPermissionMap]] = Content(
            data=found_entities,
            message="AccountPermissionMap read all succeed."
        )
    except Exception as exception:
        content: Content[List[AccountPermissionMap]] = Content(
            data=None,
            message=f"AccountPermissionMap read all failed: {exception}"
        )
    return content


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[AccountPermissionMap]:
    try:
        found_entity: AccountPermissionMap = await account_permission_map_repository.read_one_by_id(request.id)
        content: Content[AccountPermissionMap] = Content(
            data=found_entity,
            message="AccountPermissionMap read one by id succeed."
        )
    except Exception as exception:
        content: Content[AccountPermissionMap] = Content(
            data=None,
            message=f"AccountPermissionMap read one by id failed: {exception}"
        )
    return content


async def create_one(request: CreateOneRequest) -> Content[AccountPermissionMap]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: AccountPermissionMap = AccountPermissionMap(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: AccountPermissionMap = await account_permission_map_repository.create_one(entity_to_create)
        content: Content[AccountPermissionMap] = Content(
            data=created_entity,
            message="AccountPermissionMap create one succeed."
        )
    except Exception as exception:
        content: Content[AccountPermissionMap] = Content(
            data=None,
            message=f"AccountPermissionMap create one failed: {exception}"
        )
    return content


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[AccountPermissionMap]:
    try:
        entity_to_patch: AccountPermissionMap = AccountPermissionMap(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: AccountPermissionMap = await account_permission_map_repository.patch_one_by_id(request.id,
                                                                                                       entity_to_patch)
        content: Content[AccountPermissionMap] = Content(
            data=patched_entity,
            message="AccountPermissionMap patch one by id succeed."
        )
    except Exception as exception:
        content: Content[AccountPermissionMap] = Content(
            data=None,
            message=f"AccountPermissionMap patch one by id failed: {exception}"
        )
    return content


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[AccountPermissionMap]:
    try:
        deleted_entity: AccountPermissionMap = await account_permission_map_repository.delete_one_by_id(request.id)
        content: Content[AccountPermissionMap] = Content(
            data=deleted_entity,
            message="AccountPermissionMap delete one by id succeed."
        )
    except Exception as exception:
        content: Content[AccountPermissionMap] = Content(
            data=None,
            message=f"AccountPermissionMap delete one by id failed: {exception}"
        )
    return content
