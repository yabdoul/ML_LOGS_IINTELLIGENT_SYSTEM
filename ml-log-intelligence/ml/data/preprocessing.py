from typing import Optional, Tuple

from sklearn.pipeline import Pipeline

from ml.data.read_data import load_data
from ml.features.build_features import (
    prepare_dataframe,
    split_features_target,
    validate_data_consistency,
)
from ml.features.feature_config import build_preprocessor


def run_preprocessing(
    data_path: Optional[str] = None,
    max_features: int = 500,
) -> Tuple[object, object, Pipeline]:
    df = load_data(data_path) if data_path else load_data()
    validate_data_consistency(df)
    df = prepare_dataframe(df)
    x, y = split_features_target(df)
    preprocessor = build_preprocessor(max_features=max_features)
    x_matrix = preprocessor.fit_transform(x)
    return x_matrix, y, preprocessor


if __name__ == "__main__":
    features, targets, _ = run_preprocessing()
    print(features.shape)
