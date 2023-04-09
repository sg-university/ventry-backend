from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.file import File
from app.outers.utilities.datastore_utility import DataStoreUtility


class FileRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[File]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(File)
            result = await session.execute(statement)
            found_entities: List[File] = result.scalars().all()
            return found_entities

    async def read_one_by_id(self, id: UUID) -> File:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(File).where(File.id == id)
            result = await session.execute(statement)
            found_entity: File = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: File) -> File:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: File) -> File:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(File).where(File.id == id)
                result = await session.execute(statement)
                found_entity: File = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> File:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(File).where(File.id == id)
                result = await session.execute(statement)
                found_entity: File = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
