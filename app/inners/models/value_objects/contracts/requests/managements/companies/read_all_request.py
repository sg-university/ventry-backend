from typing import Dict

from pydantic import BaseModel


class ReadAllRequest(BaseModel):
    query_parameter: Dict[str, str]
