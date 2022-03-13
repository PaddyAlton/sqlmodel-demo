# services/config.py
# manages application configuration

from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn


class AppSettings(BaseSettings):
    application_env: str
    connection_string: PostgresDsn


@lru_cache()
def get_settings() -> AppSettings:
    return AppSettings()
