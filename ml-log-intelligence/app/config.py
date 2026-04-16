from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str

    model_path: str

    alert_webhook: str

    env: str = "development"
    log_level: str = "info"

    model_config = ConfigDict(
        env_file=Path(__file__).resolve().parent / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
