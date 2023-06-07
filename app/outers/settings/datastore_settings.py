import os
from typing import Optional

from pydantic import BaseSettings


class DatastoreSetting(BaseSettings):
    DS_DIALECT: str = os.environ.get("DS_DIALECT")
    DS_HOST: str = os.environ.get("DS_HOST")
    DS_PORT: str = os.environ.get("DS_PORT")
    DS_USER: str = os.environ.get("DS_USER")
    DS_PASSWORD: str = os.environ.get("DS_PASSWORD")
    DS_DATABASE: str = os.environ.get("DS_DATABASE")
    URL: Optional[str]

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs: any):
        super().__init__(**kwargs)
        self.URL = f"{self.DS_DIALECT}://{self.DS_USER}:{self.DS_PASSWORD}@{self.DS_HOST}:{self.DS_PORT}/{self.DS_DATABASE}"
