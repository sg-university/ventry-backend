from pydantic import BaseModel

from app.inners.models.value_objects.contracts.requests.managements.files.create_body import \
    CreateBody


class CreateOneRequest(BaseModel):
    body: CreateBody
