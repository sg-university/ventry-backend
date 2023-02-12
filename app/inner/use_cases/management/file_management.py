import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.file import File
from app.outer.interfaces.deliveries.contracts.requests.file_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.file_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import file_repository


def read_all() -> Content[List[File]]:
    entities: List[File] = file_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[File]](data=entities, message="File read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"File read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[File]:
    return rx.just(request).pipe(
        ops.map(lambda request: file_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="File read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"File read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[File]:
    return rx.just(request).pipe(
        ops.map(lambda request: File(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                     updated_at=datetime.now())),
        ops.map(lambda entity: file_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="File create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"File create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[File]:
    return rx.just(request).pipe(
        ops.map(lambda request: file_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: file_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="File patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"File patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[File]:
    return rx.just(request).pipe(
        ops.map(lambda request: file_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="File delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"File delete one by id failed: {exception}")))
    ).run()
