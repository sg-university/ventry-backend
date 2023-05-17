from app.inners.models.value_objects.base_value_object import BaseValueObject

from app.inners.models.value_objects.contracts.requests.authentications.registers.account_register import \
    AccountRegister
from app.inners.models.value_objects.contracts.requests.authentications.registers.company_register import \
    CompanyRegister
from app.inners.models.value_objects.contracts.requests.authentications.registers.location_register import \
    LocationRegister


class RegisterByEmailAndPasswordBody(BaseValueObject):
    account: AccountRegister
    company: CompanyRegister
    location: LocationRegister
