from typing import Dict

from app.inners.models.value_objects.base_value_object import BaseValueObject


class ReadAllRequest(BaseValueObject):
    query_parameter: Dict[str, str]
