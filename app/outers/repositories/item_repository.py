from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.item import Item
from app.outers.utilities.datastore_utility import DataStoreUtility


class ItemRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[Item]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Item)
            result = await session.execute(statement)
            found_entities: List[Item] = result.scalars().all()
            return found_entities

    async def read_one_by_id(self, id: UUID) -> Item:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Item).where(Item.id == id)
            result = await session.execute(statement)
            found_entity: Item = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: Item) -> Item:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: Item) -> Item:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Item).where(Item.id == id)
                result = await session.execute(statement)
                found_entity: Item = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> Item:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Item).where(Item.id == id)
                result = await session.execute(statement)
                found_entity: Item = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
