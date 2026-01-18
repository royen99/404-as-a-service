"""
Application configuration using Pydantic settings.
Reads from environment variables with sensible defaults.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App settings
    app_name: str = "404-as-a-Service"
    debug: bool = False

    # Data paths
    reasons_file: str = "data/reasons.json"

    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Cache settings to avoid reading .env multiple times."""
    return Settings()


settings = get_settings()
