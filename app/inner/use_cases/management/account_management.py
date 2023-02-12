import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.account import Account
from app.outer.interfaces.deliveries.contracts.requests.account_management.create_one_request import CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.account_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import account_repository


def read_all() -> Content[List[Account]]:
    entities: List[Account] = account_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[Account]](data=entities, message="Account read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Account read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[Account]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Account read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Account read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[Account]:
    return rx.just(request).pipe(
        ops.map(lambda request: Account(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                        updated_at=datetime.now())),
        ops.map(lambda entity: account_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="Account create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Account create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Account]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: account_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="Account patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Account patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Account]:
    return rx.just(request).pipe(
        ops.map(lambda request: account_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Account delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Account delete one by id failed: {exception}")))
    ).run()
