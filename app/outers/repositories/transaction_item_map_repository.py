from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.models.value_objects.transaction_item_map_forecast import TransactionItemMapForecast
from app.outers.utilities.datastore_utility import DataStoreUtility


class TransactionItemMapRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[TransactionItemMap]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(TransactionItemMap)
            result = await session.execute(statement)
            found_entities: List[TransactionItemMap] = result.scalars().all()
            return found_entities

    async def read_all_by_item_id(self, item_id: UUID) -> List[TransactionItemMapForecast]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(f"""
                select      tim.transaction_id, 
                            tim.item_id, 
                            sum(tim.quantity) as quantity,
                            (select     t.timestamp 
                                from    transaction t
                                where   t.id = tim.transaction_id
                            ) as timestamp
                from        transaction_item_map tim
                where       tim.item_id = '{item_id}'
                group by    tim.item_id, tim.transaction_id
                order by    timestamp asc;
            """)
            result = await session.execute(statement)
            found_entities: List[TransactionItemMapForecast] = [TransactionItemMapForecast(**x) for x in
                                                                result.fetchall()]
            return found_entities

    async def read_one_by_id(self, id: UUID) -> TransactionItemMap:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(TransactionItemMap).where(TransactionItemMap.id == id)
            result = await session.execute(statement)
            found_entity: TransactionItemMap = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: TransactionItemMap) -> TransactionItemMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: TransactionItemMap) -> TransactionItemMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(TransactionItemMap).where(TransactionItemMap.id == id)
                result = await session.execute(statement)
                found_entity: TransactionItemMap = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> TransactionItemMap:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(TransactionItemMap).where(TransactionItemMap.id == id)
                result = await session.execute(statement)
                found_entity: TransactionItemMap = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
