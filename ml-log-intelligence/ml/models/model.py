from sklearn.ensemble import IsolationForest


def build_isolation_forest():
    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        max_samples="auto",
        max_features=1.0,
        bootstrap=False,
        n_jobs=-1,
        random_state=42,
    )
    return model
