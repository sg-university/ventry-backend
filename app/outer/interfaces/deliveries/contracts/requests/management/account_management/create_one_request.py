from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.account_management.account_create_body import \
    AccountCreateBody


class CreateOneRequest(BaseModel):
    entity: AccountCreateBody
