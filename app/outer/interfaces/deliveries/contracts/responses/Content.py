from typing import TypeVar, Generic, Optional

from pydantic.generics import GenericModel

T = TypeVar("T")


class Content(GenericModel, Generic[T]):
    message: str
    data: Optional[T]
