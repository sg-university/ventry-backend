import os
from typing import Optional

from pydantic import BaseSettings


class DatastoreSetting(BaseSettings):
    DS_DIALECT: str = os.getenv("DS_DIALECT")
    DS_HOST: str = os.getenv("DS_HOST")
    DS_PORT: str = os.getenv("DS_PORT")
    DS_USER: str = os.getenv("DS_USER")
    DS_PASSWORD: str = os.getenv("DS_PASSWORD")
    DS_DATABASE: str = os.getenv("DS_DATABASE")
    URL: Optional[str]

    def __init__(self, **kwargs: any):
        super().__init__(**kwargs)
        self.URL = f"{self.DS_DIALECT}://{self.DS_USER}:{self.DS_PASSWORD}@{self.DS_HOST}:{self.DS_PORT}/{self.DS_DATABASE}"
