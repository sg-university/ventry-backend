from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.role_management.role_create import RoleCreate


class CreateOneRequest(BaseModel):
    entity: RoleCreate
