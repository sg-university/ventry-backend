import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import account_permission_map_repository


def read_all() -> Content[List[AccountPermissionMap]]:
    entities: List[AccountPermissionMap] = account_permission_map_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[AccountPermissionMap]](data=entities,
                                                                     message="AccountPermissionMap read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"AccountPermissionMap read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[AccountPermissionMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_permission_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="AccountPermissionMap read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"AccountPermissionMap read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[AccountPermissionMap]:
    return rx.just(request).pipe(
        ops.map(
            lambda request: AccountPermissionMap(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                                 updated_at=datetime.now())),
        ops.map(lambda entity: account_permission_map_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="AccountPermissionMap create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"AccountPermissionMap create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[AccountPermissionMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_permission_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: account_permission_map_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="AccountPermissionMap patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"AccountPermissionMap patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[AccountPermissionMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_permission_map_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="AccountPermissionMap delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"AccountPermissionMap delete one by id failed: {exception}")))
    ).run()
