from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl

    DEBUG: bool = False
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    SECRET_KEY: str

    # 60 seconds * 60 minutes * 2 hours = 2 hours
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 2

    DATABASE_URI: str
    DATABASE_NAME: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
