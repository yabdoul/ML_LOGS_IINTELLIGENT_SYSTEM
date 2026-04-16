from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    db_url: str

    # ML model
    model_path: str

    # Alerts
    alert_webhook: str

    # App settings
    env: str = "development"
    log_level: str = "info"

    model_config = ConfigDict(
        env_file=Path(__file__).resolve().parent / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
