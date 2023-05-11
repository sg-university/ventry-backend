from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.sql import expression

from app.inners.models.entities.role import Role
from app.outers.utilities.datastore_utility import DataStoreUtility


class RoleRepository:
    def __init__(self):
        self.datastore_utility: DataStoreUtility = DataStoreUtility()

    async def read_all(self) -> List[Role]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Role)
            result = await session.execute(statement)
            found_entities: List[Role] = result.scalars().all()
            return found_entities

    async def read_all_by_account_id(self, account_id: UUID) -> List[Role]:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = text(
                f"""
                SELECT r.*
                FROM role r
                INNER JOIN account a on a.role_id = r.id
                WHERE a.id = '{account_id}'
                """
            )
            result = await session.execute(statement)
            found_entities: List[Role] = [Role(**entity) for entity in result.fetchall()]
            return found_entities
    
    async def read_one_by_id(self, id: UUID) -> Role:
        async with await self.datastore_utility.create_session() as session:
            statement: expression = select(Role).where(Role.id == id)
            result = await session.execute(statement)
            found_entity: Role = result.scalars().one()
            if found_entity is None:
                raise Exception("Entity not found.")
            return found_entity

    async def create_one(self, entity: Role) -> Role:
        async with await self.datastore_utility.create_session() as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
            except Exception as exception:
                raise exception
        return entity

    async def patch_one_by_id(self, id: UUID, entity: Role) -> Role:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Role).where(Role.id == id)
                result = await session.execute(statement)
                found_entity: Role = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                found_entity.patch_from(entity.dict())
                await session.commit()
                await session.refresh(found_entity)
            except Exception as exception:
                raise exception
            return found_entity

    async def delete_one_by_id(self, id: UUID) -> Role:
        async with await self.datastore_utility.create_session() as session:
            try:
                statement: expression = select(Role).where(Role.id == id)
                result = await session.execute(statement)
                found_entity: Role = result.scalars().one()
                if found_entity is None:
                    raise Exception("Entity not found.")
                await session.delete(found_entity)
                await session.commit()
            except Exception as exception:
                raise exception
            return found_entity
