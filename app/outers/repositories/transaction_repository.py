from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.transaction import Transaction
from app.outers.utilities.datastore_utility import DataStoreUtility


class TransactionRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[Transaction]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Transaction)
            result = await session.execute(statement)
            found_entities: List[Transaction] = result.scalars().all()
            return found_entities

    async def read_one_by_id(self, id: UUID) -> Transaction:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Transaction).where(Transaction.id == id)
            result = await session.execute(statement)
            found_entity: Transaction = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: Transaction) -> Transaction:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: Transaction) -> Transaction:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Transaction).where(Transaction.id == id)
                result = await session.execute(statement)
                found_entity: Transaction = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> Transaction:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Transaction).where(Transaction.id == id)
                result = await session.execute(statement)
                found_entity: Transaction = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
