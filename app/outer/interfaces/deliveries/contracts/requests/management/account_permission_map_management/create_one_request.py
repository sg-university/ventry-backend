from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.account_permission_map_management.account_permission_map_create_body import \
    AccountPermissionMapCreateBody


class CreateOneRequest(BaseModel):
    entity: AccountPermissionMapCreateBody
