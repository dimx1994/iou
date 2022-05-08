from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    decimal_digits = 3

    class Config:
        env_prefix = ''


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings()
