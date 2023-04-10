import functools

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Class to use environment variables.
    """

    API_ADDRESS: str = "localhost:8000"
    API_DESCRIPTION: str = "Mautualizo Test API"
    API_TITTLE: str = "Mautualizo API"
    API_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"


@functools.lru_cache
def get_settings() -> Settings:
    """
    Get global settings object (cached for performance).
    """
    return Settings()
