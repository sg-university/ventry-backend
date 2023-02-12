from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class AccountPermissionMap(SQLModel, table=True):
    __tablename__ = "account_permission_map"
    id: UUID = Field(primary_key=True)
    account_id: UUID = Field(foreign_key="account.id")
    permission_id: UUID = Field(foreign_key="permission.id")
    created_at: datetime
    updated_at: datetime

    def patch_from(self, entity: AccountPermissionMap):
        self.id = entity.id
        self.account_id = entity.account_id
        self.permission_id = entity.permission_id
        self.created_at = entity.created_at
        self.updated_at = entity.updated_at
