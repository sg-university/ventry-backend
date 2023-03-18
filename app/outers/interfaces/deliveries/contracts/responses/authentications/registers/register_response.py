from pydantic import BaseModel

from app.inners.models.entities.account import Account


class RegisterResponse(BaseModel):
    entity: Account
