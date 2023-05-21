from typing import List

from app.inners.models.value_objects.base_value_object import BaseValueObject
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_transaction_body import \
    CheckoutTransactionBody
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_transaction_item_map_body import \
    CheckoutTransactionItemMapBody


class CheckoutBody(BaseValueObject):
    transaction: CheckoutTransactionBody
    transaction_item_maps: List[CheckoutTransactionItemMapBody]
    is_record_to_inventory_controls: bool
