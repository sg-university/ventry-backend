import uuid
from datetime import datetime
from typing import List

from app.inner.models.entities.file import File
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.management.file_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import file_repository


async def read_all() -> Content[List[File]]:
    try:
        found_entities: List[File] = await file_repository.read_all()
        content: Content[List[File]] = Content(
            data=found_entities,
            message="File read all succeed."
        )
    except Exception as exception:
        content: Content[List[File]] = Content(
            data=None,
            message=f"File read all failed: {exception}"
        )
    return content


async def read_one_by_id(request: ReadOneByIdRequest) -> Content[File]:
    try:
        found_entity: File = await file_repository.read_one_by_id(request.id)
        content: Content[File] = Content(
            data=found_entity,
            message="File read one by id succeed."
        )
    except Exception as exception:
        content: Content[File] = Content(
            data=None,
            message=f"File read one by id failed: {exception}"
        )
    return content


async def create_one(request: CreateOneRequest) -> Content[File]:
    try:
        timestamp: datetime = datetime.now()
        entity_to_create: File = File(
            **request.entity.dict(),
            id=uuid.uuid4(),
            created_at=timestamp,
            updated_at=timestamp,
        )
        created_entity: File = await file_repository.create_one(entity_to_create)
        content: Content[File] = Content(
            data=created_entity,
            message="File create one succeed."
        )
    except Exception as exception:
        content: Content[File] = Content(
            data=None,
            message=f"File create one failed: {exception}"
        )
    return content


async def patch_one_by_id(request: PatchOneByIdRequest) -> Content[File]:
    try:
        entity_to_patch: File = File(
            **request.entity.dict(),
            id=request.id,
            updated_at=datetime.now(),
        )
        patched_entity: File = await file_repository.patch_one_by_id(request.id, entity_to_patch)
        content: Content[File] = Content(
            data=patched_entity,
            message="File patch one by id succeed."
        )
    except Exception as exception:
        content: Content[File] = Content(
            data=None,
            message=f"File patch one by id failed: {exception}"
        )
    return content


async def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[File]:
    try:
        deleted_entity: File = await file_repository.delete_one_by_id(request.id)
        content: Content[File] = Content(
            data=deleted_entity,
            message="File delete one by id succeed."
        )
    except Exception as exception:
        content: Content[File] = Content(
            data=None,
            message=f"File delete one by id failed: {exception}"
        )
    return content
