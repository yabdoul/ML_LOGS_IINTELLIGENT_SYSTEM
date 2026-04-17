from typing import List

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TEXT_COLUMN = "message"
TIMESTAMP_COLUMN = "timestamp"
TARGET_COLUMN = "is_anomaly"

CATEGORICAL_COLUMNS: List[str] = ["level", "service_name"]
NUMERIC_COLUMNS: List[str] = [
    "latency_ms",
    "status_code",
    "hour_of_day",
    "day_of_week",
]

OPTIONAL_COLUMNS: List[str] = ["request_id", "anomaly_type"]
REQUIRED_COLUMNS: List[str] = [
    TEXT_COLUMN,
    TIMESTAMP_COLUMN,
    TARGET_COLUMN,
    *CATEGORICAL_COLUMNS,
    "latency_ms",
    "status_code",
]


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df[TIMESTAMP_COLUMN] = pd.to_datetime(
        df[TIMESTAMP_COLUMN],
        errors="coerce",
    )
    df["hour_of_day"] = df[TIMESTAMP_COLUMN].dt.hour
    df["day_of_week"] = df[TIMESTAMP_COLUMN].dt.dayofweek
    return df


def build_preprocessor(max_features: int = 500) -> Pipeline:
    text_transformer = TfidfVectorizer(max_features=max_features)
    one_hot_transformer = OneHotEncoder(handle_unknown="ignore")
    transformer = ColumnTransformer(
        transformers=[
            ("text", text_transformer, TEXT_COLUMN),
            ("oh", one_hot_transformer, CATEGORICAL_COLUMNS),
            ("num", StandardScaler(), NUMERIC_COLUMNS),
        ]
    )
    return Pipeline(steps=[("transform", transformer)])
