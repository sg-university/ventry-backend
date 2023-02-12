import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.item import Item
from app.outer.interfaces.deliveries.contracts.requests.item_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_repository


def read_all() -> Content[List[Item]]:
    entities: List[Item] = item_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[Item]](data=entities,
                                                     message="Item read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Item read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[Item]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Item read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Item read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[Item]:
    return rx.just(request).pipe(
        ops.map(lambda request: Item(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                     updated_at=datetime.now())),
        ops.map(lambda entity: item_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="Item create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Item create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[Item]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: item_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="Item patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Item patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[Item]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="Item delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"Item delete one by id failed: {exception}")))
    ).run()
