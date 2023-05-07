from pydantic import BaseModel

from app.outers.interfaces.deliveries.contracts.requests.managements.companies.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
