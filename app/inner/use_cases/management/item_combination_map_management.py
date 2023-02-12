import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.item_combination_map import ItemCombinationMap
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.item_combination_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import item_combination_map_repository


def read_all() -> Content[List[ItemCombinationMap]]:
    entities: List[ItemCombinationMap] = item_combination_map_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[ItemCombinationMap]](data=entities,
                                                                   message="ItemCombinationMap read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemCombinationMap read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[ItemCombinationMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_combination_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="ItemCombinationMap read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemCombinationMap read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[ItemCombinationMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: ItemCombinationMap(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                                   updated_at=datetime.now())),
        ops.map(lambda entity: item_combination_map_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="ItemCombinationMap create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemCombinationMap create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[ItemCombinationMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_combination_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: item_combination_map_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="ItemCombinationMap patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemCombinationMap patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[ItemCombinationMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: item_combination_map_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="ItemCombinationMap delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"ItemCombinationMap delete one by id failed: {exception}")))
    ).run()
