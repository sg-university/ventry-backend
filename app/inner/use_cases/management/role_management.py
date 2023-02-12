import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.role import Role
from app.outer.interfaces.deliveries.contracts.requests.role_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.role_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.role_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.role_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import role_repository


def read_all() -> Content[List[Role]]:
    entities: List[Role] = role_repository.read_all()
    return rx.from_list(entities).pipe(
        ops.to_list(),
        ops.map(lambda entity: Content[List[Role]](data=entity, message="Role read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Role read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[Role]:
    return rx.just(request).pipe(
        ops.map(lambda request: role_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Role read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Role read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[Role]:
    return rx.just(request).pipe(
        ops.map(lambda request: Role(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                     updated_at=datetime.now())),
        ops.map(lambda entity: role_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="Role create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Role create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Role]:
    def patch_from(entity: Role) -> Role:
        entity.id = request.id
        entity.name = request.entity.name
        entity.description = request.entity.description
        entity.updated_at = datetime.now()
        return entity

    return rx.just(request).pipe(
        ops.map(lambda request: role_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: patch_from(entity)),
        ops.map(lambda entity: role_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="Role patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Role patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Role]:
    return rx.just(request).pipe(
        ops.map(lambda request: role_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Role delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Role delete one by id failed: {exception}")))
    ).run()
