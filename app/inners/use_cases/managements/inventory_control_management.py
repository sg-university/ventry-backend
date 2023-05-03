import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.inventory_control import InventoryControl
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.create_one_request import \
    CreateOneRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.outers.interfaces.deliveries.contracts.requests.managements.inventory_controls.read_one_by_id_request import \
    ReadOneByIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.repositories.inventory_control_repository import InventoryControlRepository


class InventoryControlManagement:
    def __init__(self):
        self.inventory_control_repository: InventoryControlRepository = InventoryControlRepository()

    async def read_all(self) -> Content[List[InventoryControl]]:
        try:
            found_entities: List[InventoryControl] = await self.inventory_control_repository.read_all()
            content: Content[List[InventoryControl]] = Content(
                data=found_entities,
                message="InventoryControl read all succeed."
            )
        except Exception as exception:
            content: Content[List[InventoryControl]] = Content(
                data=None,
                message=f"InventoryControl read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[InventoryControl]:
        try:
            found_entity: InventoryControl = await self.inventory_control_repository.read_one_by_id(request.id)
            content: Content[InventoryControl] = Content(
                data=found_entity,
                message="InventoryControl read one by id succeed."
            )
        except Exception as exception:
            content: Content[InventoryControl] = Content(
                data=None,
                message=f"InventoryControl read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[InventoryControl]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: InventoryControl = InventoryControl(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: InventoryControl = await self.inventory_control_repository.create_one(entity_to_create)
            content: Content[InventoryControl] = Content(
                data=created_entity,
                message="InventoryControl create one succeed."
            )
        except Exception as exception:
            content: Content[InventoryControl] = Content(
                data=None,
                message=f"InventoryControl create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[InventoryControl]:
        try:
            entity_to_patch: InventoryControl = InventoryControl(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: InventoryControl = await self.inventory_control_repository.patch_one_by_id(request.id,
                                                                                                       entity_to_patch)
            content: Content[InventoryControl] = Content(
                data=patched_entity,
                message="InventoryControl patch one by id succeed."
            )
        except Exception as exception:
            content: Content[InventoryControl] = Content(
                data=None,
                message=f"InventoryControl patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[InventoryControl]:
        try:
            deleted_entity: InventoryControl = await self.inventory_control_repository.delete_one_by_id(request.id)
            content: Content[InventoryControl] = Content(
                data=deleted_entity,
                message="InventoryControl delete one by id succeed."
            )
        except Exception as exception:
            content: Content[InventoryControl] = Content(
                data=None,
                message=f"InventoryControl delete one by id failed: {exception}"
            )
        return content
