import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.item_file_map import ItemFileMap
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_file_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_file_map_repository


def read_all() -> Content[List[ItemFileMap]]:
    entities: List[ItemFileMap] = item_file_map_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[ItemFileMap]](data=entities, message="ItemFileMap read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemFileMap read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[ItemFileMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_file_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="ItemFileMap read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemFileMap read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[ItemFileMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: ItemFileMap(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                            updated_at=datetime.now())),
        ops.map(lambda entity: item_file_map_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="ItemFileMap create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemFileMap create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[ItemFileMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_file_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: item_file_map_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="ItemFileMap patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemFileMap patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[ItemFileMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_file_map_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="ItemFileMap delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemFileMap delete one by id failed: {exception}")))
    ).run()
