from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class LogEntry(BaseModel):
    timestramp: datetime = Field(default_factory=datetime.now)
    level: Literal["INFO", "WARN", "ERROR", "CRITICAL"]
    service_name: str = Field(min_length=3)
    message: str = Field(min_length=3)
    request_id: str = Field(min_length=3)
    latency_ms: int
    status_code: int

    @field_validator("latency_ms")
    @classmethod
    def validate_latency(cls, v):
        if v <= 0:
            raise ValueError("invalid Latency")
        return v

    @field_validator("status_code")
    @classmethod
    def validate_status(cls, v):
        if v < 100 or v > 599:
            raise ValueError("status_code must be a valid HTTP code (100–599)")
        return v
