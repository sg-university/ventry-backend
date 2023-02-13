import uuid
from datetime import datetime
from typing import List

import reactivex as rx
from reactivex import operators as ops

from app.inner.models.entities.inventory_control import InventoryControl
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outer.interfaces.deliveries.contracts.requests.inventory_control_management.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.repositories import inventory_control_repository


def read_all() -> Content[List[InventoryControl]]:
    entities: List[InventoryControl] = inventory_control_repository.read_all()
    return rx.just(entities).pipe(
        ops.map(lambda entities: Content[List[InventoryControl]](data=entities,
                                                                 message="InventoryControl read all succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"InventoryControl read all failed: {exception}")))
    ).run()


def read_one_by_id(request: ReadOneByIdRequest) -> Content[InventoryControl]:
    return rx.just(request).pipe(
        ops.map(lambda request: inventory_control_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="InventoryControl read one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"InventoryControl read one by id failed: {exception}")))
    ).run()


def create_one(request: CreateOneRequest) -> Content[InventoryControl]:
    return rx.just(request).pipe(
        ops.map(lambda request: InventoryControl(**request.entity.dict(), id=uuid.uuid4(), created_at=datetime.now(),
                                                 updated_at=datetime.now())),
        ops.map(lambda entity: inventory_control_repository.create_one(entity)),
        ops.map(lambda entity: Content(data=entity, message="InventoryControl create one succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"InventoryControl create one failed: {exception}")))
    ).run()


def patch_one_by_id(request: PatchOneByIdRequest) -> Content[InventoryControl]:
    return rx.just(request).pipe(
        ops.map(lambda request: inventory_control_repository.read_one_by_id(request.id)),
        ops.map(lambda entity: entity.patch_from(request.entity.dict())),
        ops.map(lambda entity: inventory_control_repository.patch_one_by_id(request.id, entity)),
        ops.map(lambda entity: Content(data=entity, message="InventoryControl patch one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"InventoryControl patch one by id failed: {exception}")))
    ).run()


def delete_one_by_id(request: DeleteOneByIdRequest) -> Content[InventoryControl]:
    return rx.just(request).pipe(
        ops.map(lambda request: inventory_control_repository.delete_one_by_id(request.id)),
        ops.map(lambda entity: Content(data=entity, message="InventoryControl delete one by id succeed.")),
        ops.catch(lambda exception, source: rx.just(
            Content(entity=None, message=f"InventoryControl delete one by id failed: {exception}")))
    ).run()
