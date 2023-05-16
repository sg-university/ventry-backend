from pydantic import BaseModel

from app.inners.models.value_objects.contracts.requests.authentications.registers.account_register import \
    AccountRegister
from app.inners.models.value_objects.contracts.requests.authentications.registers.company_register import \
    CompanyRegister
from app.inners.models.value_objects.contracts.requests.authentications.registers.location_register import \
    LocationRegister


class RegisterByEmailAndPasswordRequest(BaseModel):
    account: AccountRegister
    company: CompanyRegister
    location: LocationRegister
