import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

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


def read_all() -> Content[List[Permission]]:
    entities: List[Permission] = permission_repository.read_all()
    return rx.from_list(entities).pipe(
        ops.to_list(),
        ops.map(lambda entity: Content[List[Permission]](data=entity, message="Permission read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Permission read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[Permission]:
    return rx.just(request).pipe(
        ops.map(lambda request: permission_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Permission read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Permission read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[Permission]:
    return rx.just(request).pipe(
        ops.map(lambda request: Permission(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                           updated_at=datetime.now())),
        ops.map(lambda entity: permission_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="Permission create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Permission create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Permission]:
    def patch_from(entity: Permission) -> Permission:
        entity.id = request.id
        entity.name = request.entity.name
        entity.description = request.entity.description
        entity.updated_at = datetime.now()
        return entity

    return rx.just(request).pipe(
        ops.map(lambda request: permission_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: patch_from(entity)),
        ops.map(lambda entity: permission_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="Permission patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Permission patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Permission]:
    return rx.just(request).pipe(
        ops.map(lambda request: permission_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Permission delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Permission delete one by id failed: {exception}")))
    ).run()
