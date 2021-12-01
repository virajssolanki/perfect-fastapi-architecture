from pydantic import PostgresDsn
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "FASTAPI architecture"

    database_url: PostgresDsn

    class Config(AppSettings.Config):
        env_file = ".env"