"""
Model Evaluation Script
Loads the trained model and test data, evaluates performance, and checks model behavior.
"""

from pathlib import Path

import joblib
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def load_model_and_test_data():
    """Load the trained model and test data from disk."""
    models_dir = Path(__file__).resolve().parent

    model = joblib.load(models_dir / "isolation_forest_model.pkl")
    print(f"[INFO] Model loaded from: {models_dir / 'isolation_forest_model.pkl'}")

    x_test = joblib.load(models_dir / "x_test.pkl")
    y_test = joblib.load(models_dir / "y_test.pkl")
    print(f"[INFO] Test data loaded. Shape: {x_test.shape}")

    return model, x_test, y_test


def evaluate_model(model, x_test, y_test):
    """Evaluate the model on test data."""
    print("[INFO] Evaluating model performance...")

    scores = model.decision_function(x_test)

    threshold = 0
    y_pred = (scores < threshold).astype(int)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label=1, zero_division=0)
    recall = recall_score(y_test, y_pred, pos_label=1, zero_division=0)
    f1 = f1_score(y_test, y_pred, pos_label=1, zero_division=0)

    # print(f"[EVALUATION RESULTS]")
    # print(f"Accuracy:  {accuracy:.4f}")
    # print(f"Precision: {precision:.4f}")
    # print(f"Recall:    {recall:.4f}")
    # print(f"F1-Score:  {f1:.4f}")

    print("\nDetailed Classification Report:")
    print(
        classification_report(y_test, y_pred, target_names=["Normal", "Anomaly"], zero_division=0)
    )

    cm = confusion_matrix(y_test, y_pred)
    # print(f"\nConfusion Matrix:")
    print(cm)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "predictions": y_pred,
        "decision_scores": scores,
    }


def check_model_behavior(model, x_test, y_test, results):
    """Check model behavior and provide insights."""
    print("\n[MODEL BEHAVIOR ANALYSIS]")

    predicted_anomalies = results["predictions"].sum()
    actual_anomalies = y_test.sum() if hasattr(y_test, "sum") else sum(y_test)

    print(f"Actual anomalies in test set: {actual_anomalies}")
    print(f"Predicted anomalies: {predicted_anomalies}")
    print(f"Total test samples: {len(y_test)}")

    decision_scores = results["decision_scores"]
    anomaly_mask = y_test == 1
    normal_mask = y_test == 0

    if anomaly_mask.any():
        print(f"Average decision score for anomalies: {decision_scores[anomaly_mask].mean():.4f}")
    else:
        print("No actual anomalies in test set")

    if normal_mask.any():
        print(
            f"Average decision score for normal samples: {decision_scores[normal_mask].mean():.4f}"
        )
    else:
        print("No normal samples in test set")
    avg_decision_score = decision_scores.mean()
    print(f"Average decision score on test set: {avg_decision_score:.4f}")


def main():
    """Main evaluation workflow."""
    print("=" * 50)
    print("STARTING MODEL EVALUATION")
    print("=" * 50)

    model, x_test, y_test = load_model_and_test_data()

    results = evaluate_model(model, x_test, y_test)

    check_model_behavior(model, x_test, y_test, results)

    print("=" * 50)
    print("MODEL EVALUATION COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()
