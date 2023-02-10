from typing import List
from uuid import UUID

from sqlmodel import select
from sqlmodel.sql import expression

from app.inner.models.entities.role import Role
from app.outer.utilities import datastore_utility


def read_all() -> List[Role]:
    with datastore_utility.create_session() as session:
        statement: expression = select(Role)
        found_entities: List[Role] = session.exec(statement).all()
        return found_entities


def read_one_by_id(id: UUID) -> Role:
    with datastore_utility.create_session() as session:
        statement: expression = select(Role).where(Role.id == id)
        found_entity: Role = session.exec(statement).first()
        if found_entity is None:
            raise Exception("Entity not found.")
        return found_entity


def create_one(entity: Role) -> Role:
    with datastore_utility.create_session() as session:
        try:
            session.add(entity)
            session.commit()
            session.refresh(entity)
        except Exception as e:
            raise e
    return entity


def patch_one_by_id(id: UUID, entity: Role) -> Role:
    with datastore_utility.create_session() as session:
        try:
            statement: expression = select(Role).where(Role.id == id)
            found_entity: Role = session.exec(statement).first()
            if found_entity is None:
                raise Exception("Entity not found.")
            found_entity.id = entity.id
            found_entity.name = entity.name
            found_entity.description = entity.description
            found_entity.created_at = entity.created_at
            found_entity.updated_at = entity.updated_at
            session.commit()
            session.refresh(found_entity)
        except Exception as e:
            raise e
        return found_entity


def delete_one_by_id(id: UUID) -> Role:
    with datastore_utility.create_session() as session:
        try:
            statement: expression = select(Role).where(Role.id == id)
            found_entity: Role = session.exec(statement).first()
            if found_entity is None:
                raise Exception("Entity not found.")
            session.delete(found_entity)
            session.commit()
        except Exception as e:
            raise e
        return found_entity
