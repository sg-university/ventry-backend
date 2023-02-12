from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.account_permission_map_management.account_permission_map_create import \
    AccountPermissionMapCreate


class CreateOneRequest(BaseModel):
    entity: AccountPermissionMapCreate
