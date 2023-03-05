from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_management.transaction_create_body import \
    TransactionCreateBody


class CreateOneRequest(BaseModel):
    entity: TransactionCreateBody
