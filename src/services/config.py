# services/config.py
# manages application configuration

from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn
from typing import Literal


class AppSettings(BaseSettings):
    application_env: str
    connection_string: PostgresDsn | Literal["sqlite:///test.db"]


@lru_cache()
def get_settings() -> AppSettings:
    return AppSettings()
