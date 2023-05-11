from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.location import Location
from app.outers.utilities.datastore_utility import DataStoreUtility


class LocationRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[Location]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Location)
            result = await session.execute(statement)
            found_entities: List[Location] = result.scalars().all()
            return found_entities

    async def read_all_by_account_id(self, account_id: UUID) -> List[Location]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(
                f"""
                SELECT l.*
                FROM location l
                INNER JOIN account a on a.location_id = l.id
                WHERE a.id = '{account_id}'
                """
            )
            result = await session.execute(statement)
            found_entities: List[Location] = [Location(**entity) for entity in result.fetchall()]
            return found_entities

    async def read_all_by_company_id(self, company_id: UUID) -> List[Location]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(
                f"""
                SELECT l.*
                FROM location l
                INNER JOIN company c on c.id = l.company_id
                WHERE c.id = '{company_id}'
                """
            )
            result = await session.execute(statement)
            found_entities: List[Location] = [Location(**entity) for entity in result.fetchall()]
            return found_entities

    async def read_all_by_item_id(self, item_id: UUID) -> List[Location]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(
                f"""
                SELECT l.*
                FROM location l
                INNER JOIN item i on i.location_id = l.id
                WHERE i.id = '{item_id}'
                """
            )
            result = await session.execute(statement)
            found_entities: List[Location] = [Location(**entity) for entity in result.fetchall()]
            return found_entities

    async def read_one_by_id(self, id: UUID) -> Location:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Location).where(Location.id == id)
            result = await session.execute(statement)
            found_entity: Location = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: Location) -> Location:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: Location) -> Location:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Location).where(Location.id == id)
                result = await session.execute(statement)
                found_entity: Location = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> Location:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Location).where(Location.id == id)
                result = await session.execute(statement)
                found_entity: Location = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
