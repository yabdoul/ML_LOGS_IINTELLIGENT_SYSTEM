from typing import Tuple

import pandas as pd

from ml.features.feature_config import (
    OPTIONAL_COLUMNS,
    REQUIRED_COLUMNS,
    TARGET_COLUMN,
    TIMESTAMP_COLUMN,
    add_time_features,
)


def validate_columns(df: pd.DataFrame) -> None:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_data_consistency(df: pd.DataFrame) -> None:
    validate_columns(df)
    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("Null values detected in required columns")
    unique_targets = set(df[TARGET_COLUMN].dropna().unique().tolist())
    if not unique_targets.issubset({0, 1, True, False}):
        raise ValueError("Target column must be binary")


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    df = add_time_features(df)
    df = df.drop(
        columns=[TIMESTAMP_COLUMN, *OPTIONAL_COLUMNS],
        errors="ignore",
    )
    return df


def split_features_target(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    y = df[TARGET_COLUMN].astype(int)
    x = df.drop(columns=[TARGET_COLUMN])
    return x, y
