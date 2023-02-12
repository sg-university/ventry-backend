from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.account_management.account_create import AccountCreate


class CreateOneRequest(BaseModel):
    entity: AccountCreate
