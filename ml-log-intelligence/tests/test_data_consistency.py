import pandas as pd
import pytest

from ml.features.build_features import validate_data_consistency


def _sample_df():
    return pd.DataFrame(
        {
            "timestamp": ["2025-01-01T12:00:00Z", "2025-01-01T13:00:00Z"],
            "level": ["INFO", "ERROR"],
            "service_name": ["svc-a", "svc-b"],
            "message": ["ok", "fail"],
            "latency_ms": [120, 250],
            "status_code": [200, 500],
            "is_anomaly": [0, 1],
        }
    )


def test_validate_data_consistency_ok():
    df = _sample_df()
    validate_data_consistency(df)


def test_validate_data_consistency_missing_column():
    df = _sample_df().drop(columns=["message"])
    with pytest.raises(ValueError):
        validate_data_consistency(df)


def test_validate_data_consistency_non_binary_target():
    df = _sample_df()
    df.loc[0, "is_anomaly"] = 2
    with pytest.raises(ValueError):
        validate_data_consistency(df)
