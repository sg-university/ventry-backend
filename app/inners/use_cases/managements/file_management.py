import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.file import File
from app.inners.models.value_objects.contracts.requests.managements.files.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.files.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.files.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.files.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.files.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.file_repository import FileRepository
from app.outers.utilities.management_utility import ManagementUtility


class FileManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.file_repository: FileRepository = FileRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[File]]:
        try:
            found_entities: List[File] = await self.file_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "account_id" in request.query_parameter.keys():
                    found_entities = await self.file_repository.read_all_by_account_id(
                        account_id=uuid.UUID(request.query_parameter["account_id"])
                    )
                elif "item_id" in request.query_parameter.keys():
                    found_entities = await self.file_repository.read_all_by_item_id(
                        item_id=uuid.UUID(request.query_parameter["item_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[File]] = Content(
                data=found_entities,
                message="File read all succeed."
            )
        except Exception as exception:
            content: Content[List[File]] = Content(
                data=None,
                message=f"File read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[File]:
        try:
            found_entity: File = await self.file_repository.read_one_by_id(request.id)
            content: Content[File] = Content(
                data=found_entity,
                message="File read one by id succeed."
            )
        except Exception as exception:
            content: Content[File] = Content(
                data=None,
                message=f"File read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[File]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: File = File(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: File = await self.file_repository.create_one(entity_to_create)
            content: Content[File] = Content(
                data=created_entity,
                message="File create one succeed."
            )
        except Exception as exception:
            content: Content[File] = Content(
                data=None,
                message=f"File create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[File]:
        try:
            entity_to_patch: File = File(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: File = await self.file_repository.patch_one_by_id(request.id, entity_to_patch)
            content: Content[File] = Content(
                data=patched_entity,
                message="File patch one by id succeed."
            )
        except Exception as exception:
            content: Content[File] = Content(
                data=None,
                message=f"File patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[File]:
        try:
            deleted_entity: File = await self.file_repository.delete_one_by_id(request.id)
            content: Content[File] = Content(
                data=deleted_entity,
                message="File delete one by id succeed."
            )
        except Exception as exception:
            content: Content[File] = Content(
                data=None,
                message=f"File delete one by id failed: {exception}"
            )
        return content
