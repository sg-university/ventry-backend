from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.transaction_item_map_management.transaction_item_map_create import \
    TransactionItemMapCreate


class CreateOneRequest(BaseModel):
    entity: TransactionItemMapCreate
