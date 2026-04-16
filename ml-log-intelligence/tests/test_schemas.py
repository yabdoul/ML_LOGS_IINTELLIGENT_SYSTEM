import pytest
from pydantic import ValidationError

from app.api.schemas.log_entry import LogEntry


# -------------------------
# 1. VALID LOG TEST
# -------------------------
def test_valid_log_entry():
    log = LogEntry(
        level="ERROR",
        service_name="auth-service",
        message="Login failed",
        request_id="req_123",
        latency_ms=120,
        status_code=500,
    )

    assert log.level == "ERROR"
    assert log.latency_ms == 120
    assert log.status_code == 500


# -------------------------
# 2. INVALID LATENCY TEST
# -------------------------
def test_negative_latency():
    with pytest.raises(ValueError):
        LogEntry(
            level="INFO",
            service_name="auth-service",
            message="Test",
            request_id="req_123",
            latency_ms=-10,
            status_code=200,
        )


# -------------------------
# 3. INVALID STATUS CODE TEST
# -------------------------
def test_invalid_status_code():
    with pytest.raises(ValueError):
        LogEntry(
            level="INFO",
            service_name="auth-service",
            message="Test",
            request_id="req_123",
            latency_ms=50,
            status_code=999,
        )


# -------------------------
# 4. EMPTY MESSAGE TEST
# -------------------------
def test_empty_message():
    with pytest.raises(ValidationError):
        LogEntry(
            level="INFO",
            service_name="auth-service",
            message="",
            request_id="req_123",
            latency_ms=50,
            status_code=200,
        )


# -------------------------
# 5. INVALID LEVEL TEST
# -------------------------
def test_invalid_level():
    with pytest.raises(ValidationError):
        LogEntry(
            level="DEBUG",  # not allowed
            service_name="auth-service",
            message="Test",
            request_id="req_123",
            latency_ms=50,
            status_code=200,
        )
