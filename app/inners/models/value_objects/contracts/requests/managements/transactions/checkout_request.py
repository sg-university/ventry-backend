from app.inners.models.value_objects.base_value_object import BaseValueObject
from app.inners.models.value_objects.contracts.requests.managements.transactions.checkout_body import CheckoutBody


class CheckoutRequest(BaseValueObject):
    body: CheckoutBody
