import uuid
from datetime import datetime, timezone
from typing import List

from app.inners.models.entities.company import Company
from app.inners.models.value_objects.contracts.requests.managements.companies.create_one_request import \
    CreateOneRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.delete_one_by_id_request import \
    DeleteOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.patch_one_by_id_request import \
    PatchOneByIdRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.read_all_request import ReadAllRequest
from app.inners.models.value_objects.contracts.requests.managements.companies.read_one_by_id_request import \
    ReadOneByIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.outers.repositories.company_repository import CompanyRepository
from app.outers.utilities.management_utility import ManagementUtility


class CompanyManagement:
    def __init__(self):
        self.management_utility: ManagementUtility = ManagementUtility()
        self.company_repository: CompanyRepository = CompanyRepository()

    async def read_all(self, request: ReadAllRequest) -> Content[List[Company]]:
        try:
            found_entities: List[Company] = await self.company_repository.read_all()

            if len(request.query_parameter.keys()) > 0:
                if "account_id" in request.query_parameter.keys():
                    found_entities = await self.company_repository.read_all_by_account_id(
                        account_id=uuid.UUID(request.query_parameter["account_id"])
                    )
                else:
                    found_entities = list(
                        filter(
                            lambda entity: self.management_utility.filter(request.query_parameter, entity),
                            found_entities
                        )
                    )

            content: Content[List[Company]] = Content(
                data=found_entities,
                message="Company read all succeed."
            )
        except Exception as exception:
            content: Content[List[Company]] = Content(
                data=None,
                message=f"Company read all failed: {exception}"
            )
        return content

    async def read_one_by_id(self, request: ReadOneByIdRequest) -> Content[Company]:
        try:
            found_entity: Company = await self.company_repository.read_one_by_id(request.id)
            content: Content[Company] = Content(
                data=found_entity,
                message="Company read one by id succeed."
            )
        except Exception as exception:
            content: Content[Company] = Content(
                data=None,
                message=f"Company read one by id failed: {exception}"
            )
        return content

    async def create_one(self, request: CreateOneRequest) -> Content[Company]:
        try:
            timestamp: datetime = datetime.now(tz=timezone.utc)
            entity_to_create: Company = Company(
                **request.body.dict(),
                id=uuid.uuid4(),
                created_at=timestamp,
                updated_at=timestamp,
            )
            created_entity: Company = await self.company_repository.create_one(entity_to_create)
            content: Content[Company] = Content(
                data=created_entity,
                message="Company create one succeed."
            )
        except Exception as exception:
            content: Content[Company] = Content(
                data=None,
                message=f"Company create one failed: {exception}"
            )
        return content

    async def patch_one_by_id(self, request: PatchOneByIdRequest) -> Content[Company]:
        try:
            entity_to_patch: Company = Company(
                **request.body.dict(),
                id=request.id,
                updated_at=datetime.now(tz=timezone.utc),
            )
            patched_entity: Company = await self.company_repository.patch_one_by_id(request.id, entity_to_patch)
            content: Content[Company] = Content(
                data=patched_entity,
                message="Company patch one by id succeed."
            )
        except Exception as exception:
            content: Content[Company] = Content(
                data=None,
                message=f"Company patch one by id failed: {exception}"
            )
        return content

    async def delete_one_by_id(self, request: DeleteOneByIdRequest) -> Content[Company]:
        try:
            deleted_entity: Company = await self.company_repository.delete_one_by_id(request.id)
            content: Content[Company] = Content(
                data=deleted_entity,
                message="Company delete one by id succeed."
            )
        except Exception as exception:
            content: Content[Company] = Content(
                data=None,
                message=f"Company delete one by id failed: {exception}"
            )
        return content
