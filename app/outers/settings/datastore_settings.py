import os
from typing import Optional

from pydantic import BaseSettings


class DatastoreSetting(BaseSettings):
    DS_DIALECT: str
    DS_HOST: str
    DS_PORT: str
    DS_USER: str
    DS_PASSWORD: str
    DS_DATABASE: str
    URL: Optional[str]


    def __init__(self, **kwargs: any):
        super().__init__(**kwargs)
        self.DS_DIALECT = os.environ.get("DS_DIALECT")
        self.DS_HOST = os.environ.get("DS_HOST")
        self.DS_PORT = os.environ.get("DS_PORT")
        self.DS_USER = os.environ.get("DS_USER")
        self.DS_PASSWORD = os.environ.get("DS_PASSWORD")
        self.DS_DATABASE = os.environ.get("DS_DATABASE")
        self.URL = f"{self.DS_DIALECT}://{self.DS_USER}:{self.DS_PASSWORD}@{self.DS_HOST}:{self.DS_PORT}/{self.DS_DATABASE}"


