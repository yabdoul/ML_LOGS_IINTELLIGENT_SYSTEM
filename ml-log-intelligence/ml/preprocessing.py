"""Preprocessing entrypoint."""

from pathlib import Path

import joblib

from ml.data.preprocessing import run_preprocessing


def main() -> None:
    features, targets, preprocessor = run_preprocessing()
    print(features.shape)

    ml_dir = Path(__file__).resolve().parent
    models_dir = ml_dir / "models"
    models_dir.mkdir(exist_ok=True)

    # Save features, targets and preprocessor
    joblib.dump(features, models_dir / "features.pkl")
    joblib.dump(targets, models_dir / "targets.pkl")
    joblib.dump(preprocessor, models_dir / "preprocessor.pkl")

    print(f"Features shape: {features.shape}")
    print(f"Targets shape: {targets.shape}")
    print("Features, targets, and preprocessor saved successfully!")


if __name__ == "__main__":
    main()
