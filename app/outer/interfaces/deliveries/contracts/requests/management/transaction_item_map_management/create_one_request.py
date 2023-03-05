from pydantic import BaseModel

from app.outer.interfaces.deliveries.contracts.requests.management.transaction_item_map_management.transaction_item_map_create_body import \
    TransactionItemMapCreateBody


class CreateOneRequest(BaseModel):
    entity: TransactionItemMapCreateBody
