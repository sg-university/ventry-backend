from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inner.models.entities.account_permission_map import AccountPermissionMap
from app.outer.utilities import datastore_utility


def read_all() -> List[AccountPermissionMap]:
    with datastore_utility.create_session() as session:
        statement: expression = select(AccountPermissionMap)
        found_entities: List[AccountPermissionMap] = session.exec(statement).all()
        return found_entities


def read_one_by_id(id: UUID) -> AccountPermissionMap:
    with datastore_utility.create_session() as session:
        statement: expression = select(AccountPermissionMap).where(AccountPermissionMap.id == id)
        found_entity: AccountPermissionMap = session.exec(statement).one()
        if found_entity is None:
            raise Exception("Entity not found.")
        return found_entity


def create_one(entity: AccountPermissionMap) -> AccountPermissionMap:
    with datastore_utility.create_session() as session:
        try:
            session.add(entity)
            session.commit()
            session.refresh(entity)
        except Exception as e:
            raise e
    return entity


def patch_one_by_id(id: UUID, entity: AccountPermissionMap) -> AccountPermissionMap:
    with datastore_utility.create_session() as session:
        try:
            statement: expression = select(AccountPermissionMap).where(AccountPermissionMap.id == id)
            found_entity: AccountPermissionMap = session.exec(statement).first()
            if found_entity is None:
                raise Exception("Entity not found.")
            found_entity.patch_from(entity)
            session.commit()
            session.refresh(found_entity)
        except Exception as e:
            raise e
        return found_entity


def delete_one_by_id(id: UUID) -> AccountPermissionMap:
    with datastore_utility.create_session() as session:
        try:
            statement: expression = select(AccountPermissionMap).where(AccountPermissionMap.id == id)
            found_entity: AccountPermissionMap = session.exec(statement).first()
            if found_entity is None:
                raise Exception("Entity not found.")
            session.delete(found_entity)
            session.commit()
        except Exception as e:
            raise e
        return found_entity
