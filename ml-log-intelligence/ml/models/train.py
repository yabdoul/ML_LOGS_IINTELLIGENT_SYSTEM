from pathlib import Path

import joblib
from sklearn.model_selection import train_test_split

from ml.models.model import build_isolation_forest

ml_dir = Path(__file__).resolve().parent.parent
models_dir = ml_dir / "models"


def load_data():
    features = joblib.load(models_dir / "features.pkl")
    targets = joblib.load(models_dir / "targets.pkl")
    return features, targets


def validate_data(X):
    assert len(X.shape) == 2, "X must be 2D (n_samples, n_features)"
    assert X.shape[0] > 0, "Empty dataset"

    print(f"[INFO] Data validated: {X.shape}")


def train():
    x_data, y_data = load_data()

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42, stratify=y_data
    )

    validate_data(x_train)
    model = build_isolation_forest()
    print("[INFO] Training Isolation Forest...")
    model.fit(x_train)

    print("[INFO] Evaluating model on test set...")
    test_score = model.score_samples(x_test)
    print(f"[INFO] Test score calculated for {len(test_score)} samples")

    models_dir.mkdir(exist_ok=True)
    joblib.dump(model, models_dir / "isolation_forest_model.pkl")
    print(f"[INFO] Model saved to: {models_dir / 'isolation_forest_model.pkl'}")

    joblib.dump(x_test, models_dir / "x_test.pkl")
    joblib.dump(y_test, models_dir / "y_test.pkl")
    print(f"[INFO] Test data saved to: {models_dir}")

    return model


if __name__ == "__main__":
    train()
