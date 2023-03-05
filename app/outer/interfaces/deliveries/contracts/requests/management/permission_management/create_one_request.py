from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.permission_management.permission_create_body import \
    PermissionCreateBody


class CreateOneRequest(BaseModel):
    entity: PermissionCreateBody
