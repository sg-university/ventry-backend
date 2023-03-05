from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.role_management.role_create_body import \
    RoleCreateBody


class CreateOneRequest(BaseModel):
    entity: RoleCreateBody
