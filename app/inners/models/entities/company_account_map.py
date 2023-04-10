from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class CompanyAccountMap(BaseEntity, table=True):
    __tablename__ = "company_account_map"
    id: UUID = Field(primary_key=True)
    company_id: UUID = Field(foreign_key="company.id")
    account_id: UUID = Field(foreign_key="account.id")
    created_at: datetime
    updated_at: datetime
