from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.company_account_map import CompanyAccountMap
from app.outers.utilities.datastore_utility import DataStoreUtility


class CompanyAccountMapRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[CompanyAccountMap]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(CompanyAccountMap)
            result = await session.execute(statement)
            found_entities: List[CompanyAccountMap] = result.scalars().all()
            return found_entities

    async def read_one_by_id(self, id: UUID) -> CompanyAccountMap:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(CompanyAccountMap).where(CompanyAccountMap.id == id)
            result = await session.execute(statement)
            found_entity: CompanyAccountMap = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: CompanyAccountMap) -> CompanyAccountMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: CompanyAccountMap) -> CompanyAccountMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(CompanyAccountMap).where(CompanyAccountMap.id == id)
                result = await session.execute(statement)
                found_entity: CompanyAccountMap = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> CompanyAccountMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(CompanyAccountMap).where(CompanyAccountMap.id == id)
                result = await session.execute(statement)
                found_entity: CompanyAccountMap = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
