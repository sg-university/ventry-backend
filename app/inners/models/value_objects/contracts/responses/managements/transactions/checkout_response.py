from typing import List

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.entities.transaction import Transaction
from app.inners.models.entities.transaction_item_map import TransactionItemMap
from app.inners.models.value_objects.base_value_object import BaseValueObject


class CheckoutResponse(BaseValueObject):
    transaction: Transaction
    transaction_item_maps: List[TransactionItemMap]
    inventory_controls: List[InventoryControl]
