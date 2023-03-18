from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.item_file_map import ItemFileMap
from app.outers.utilities import datastore_utility


async def read_all() -> List[ItemFileMap]:
    async with await datastore_utility.create_session() as session:
        statement: expression = select(ItemFileMap)
        result = await session.execute(statement)
        found_entities: List[ItemFileMap] = result.scalars().all()
        return found_entities


async def read_one_by_id(id: UUID) -> ItemFileMap:
    async with await datastore_utility.create_session() as session:
        statement: expression = select(ItemFileMap).where(ItemFileMap.id == id)
        result = await session.execute(statement)
        found_entity: ItemFileMap = result.scalars().one()
        if found_entity is None:
            raise Exception("Entity not found.")
        return found_entity


async def create_one(entity: ItemFileMap) -> ItemFileMap:
    async with await datastore_utility.create_session() as session:
        try:
            session.add(entity)
            await session.commit()
            await session.refresh(entity)
        except Exception as exception:
            raise exception
    return entity


async def patch_one_by_id(id: UUID, entity: ItemFileMap) -> ItemFileMap:
    async with await datastore_utility.create_session() as session:
        try:
            statement: expression = select(ItemFileMap).where(ItemFileMap.id == id)
            result = await session.execute(statement)
            found_entity: ItemFileMap = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            found_entity.patch_from(entity.dict())
            await session.commit()
            await session.refresh(found_entity)
        except Exception as exception:
            raise exception
        return found_entity


async def delete_one_by_id(id: UUID) -> ItemFileMap:
    async with await datastore_utility.create_session() as session:
        try:
            statement: expression = select(ItemFileMap).where(ItemFileMap.id == id)
            result = await session.execute(statement)
            found_entity: ItemFileMap = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            await session.delete(found_entity)
            await session.commit()
        except Exception as exception:
            raise exception
        return found_entity