from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.company import Company
from app.outers.utilities.datastore_utility import DataStoreUtility


class CompanyRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[Company]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Company)
            result = await session.execute(statement)
            found_entities: List[Company] = result.scalars().all()
            return found_entities

    async def read_all_by_account_id(self, account_id: UUID) -> List[Company]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(f"""
                select c.*
                from company c
                inner join location l on l.company_id = c.id
                inner join account a on a.location_id = l.id
                where a.id = '{account_id}';
            """)
            result = await session.execute(statement)
            found_entity: List[Company] = [Company(**entity) for entity in result.fetchall()]
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def read_one_by_id(self, id: UUID) -> Company:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Company).where(Company.id == id)
            result = await session.execute(statement)
            found_entity: Company = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: Company) -> Company:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: Company) -> Company:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Company).where(Company.id == id)
                result = await session.execute(statement)
                found_entity: Company = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> Company:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Company).where(Company.id == id)
                result = await session.execute(statement)
                found_entity: Company = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
