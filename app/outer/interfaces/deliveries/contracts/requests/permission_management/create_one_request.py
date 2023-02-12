from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.permission_management.permission_create import PermissionCreate


class CreateOneRequest(BaseModel):
    entity: PermissionCreate
