from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.transaction_management.transaction_create import \
    TransactionCreate


class CreateOneRequest(BaseModel):
    entity: TransactionCreate
