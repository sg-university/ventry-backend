from pydantic import BaseModel

from app.inners.models.entities.account import Account


class LoginResponse(BaseModel):
    entity: Account
