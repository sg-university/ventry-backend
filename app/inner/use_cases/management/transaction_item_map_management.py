import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.transaction_item_map import TransactionItemMap
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import transaction_item_map_repository


def read_all() -> Content[List[TransactionItemMap]]:
    entities: List[TransactionItemMap] = transaction_item_map_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[TransactionItemMap]](data=entities,
                                                                   message="TransactionItemMap read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"TransactionItemMap read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[TransactionItemMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: transaction_item_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="TransactionItemMap read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"TransactionItemMap read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[TransactionItemMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: TransactionItemMap(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                                   updated_at=datetime.now())),
        ops.map(lambda entity: transaction_item_map_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="TransactionItemMap create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"TransactionItemMap create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[TransactionItemMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: transaction_item_map_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: transaction_item_map_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="TransactionItemMap patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"TransactionItemMap patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[TransactionItemMap]:
    return rx.just(request).pipe(
        ops.map(lambda request: transaction_item_map_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="TransactionItemMap delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"TransactionItemMap delete one by id failed: {exception}")))
    ).run()
