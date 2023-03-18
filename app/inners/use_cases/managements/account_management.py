import uuid
from datetime import datetime
from typing import List

from app.inners.models.entities.account import Account
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.accounts.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories import account_repository


async def read_all() -> Content[List[Account]]:
    try:
        found_entities: List[Account] = await account_repository.read_all()
        content: Content[List[Account]] = Content(
            data=found_entities,
            message="Account read all succeed."
        )
    except Exception as exception:
        content: Content[List[Account]] = Content(
            data=None,
            message=f"Account read all failed: {exception}"
        )
    return content


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[Account]:
    try:
        found_entity: Account = await account_repository.read_one_by_id(request.id)
        content: Content[Account] = Content(
            data=found_entity,
            message="Account read one by id succeed."
        )
    except Exception as exception:
        content: Content[Account] = Content(
            data=None,
            message=f"Account read one by id failed: {exception}"
        )
    return content


async def create_one(request: CreateOneRequest) -> Content[Account]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: Account = Account(
            **request.body.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: Account = await account_repository.create_one(entity_to_create)
        content: Content[Account] = Content(
            data=created_entity,
            message="Account create one succeed."
        )
    except Exception as exception:
        content: Content[Account] = Content(
            data=None,
            message=f"Account create one failed: {exception}"
        )
    return content


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Account]:
    try:
        entity_to_patch: Account = Account(
            **request.body.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: Account = await account_repository.patch_one_by_id(request.id, entity_to_patch)
        content: Content[Account] = Content(
            data=patched_entity,
            message="Account patch one by id succeed."
        )
    except Exception as exception:
        content: Content[Account] = Content(
            data=None,
            message=f"Account patch one by id failed: {exception}"
        )
    return content


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Account]:
    try:
        deleted_entity: Account = await account_repository.delete_one_by_id(request.id)
        content: Content[Account] = Content(
            data=deleted_entity,
            message="Account delete one by id succeed."
        )
    except Exception as exception:
        content: Content[Account] = Content(
            data=None,
            message=f"Account delete one by id failed: {exception}"
        )
    return content
