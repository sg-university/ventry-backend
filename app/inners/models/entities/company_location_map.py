from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from app.inners.models.entities.base_entity import BaseEntity


class CompanyLocationMap(BaseEntity, table=True):
    __tablename__ = "company_location_map"
    id: UUID = Field(primary_key=True)
    company_id: UUID = Field(foreign_key="company.id")
    location_id: UUID = Field(foreign_key="location.id")
    created_at: datetime
    updated_at: datetime
