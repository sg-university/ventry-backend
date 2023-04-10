from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.company_account_maps.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
