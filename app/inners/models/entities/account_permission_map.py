from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class AccountPermissionMap(BaseEntity, table=True):
    __tablename__ = "account_permission_map"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    permission_id: UUID = Field(foreign_key="permission.id")
    created_at: datetime
    updated_at: datetime
