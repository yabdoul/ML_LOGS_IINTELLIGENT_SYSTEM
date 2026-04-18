# ML Log Intelligence

An intelligent system for analyzing log data to detect anomalies using machine learning algorithms.

## Overview

The ML Log Intelligence project is designed to analyze system logs to detect anomalous patterns that could indicate system issues, security threats, or performance degradation. The system uses Isolation Forest algorithm to identify unusual log entries based on various features like latency, status codes, log levels, and message content.

## Features

- Automated anomaly detection in log data using Isolation Forest algorithm
- Comprehensive data preprocessing pipeline with TF-IDF text vectorization and feature scaling
- Train/test data splitting for proper model evaluation
- Model serialization and deserialization using joblib
- Structured log schema validation to ensure data quality
- Synthetic log generation for testing and training purposes

## Project Structure

```
ml-log-intelligence/
├── app/                 # API and core application logic
│   ├── api/             # API endpoints and schemas
│   ├── core/            # Core configuration and logging
│   ├── models/          # Model loading and prediction logic
│   ├── services/        # Business logic services
│   └── db/              # Database models and CRUD operations
├── ml/                  # Machine learning pipeline
│   ├── data/            # Data loading and preprocessing
│   ├── features/        # Feature engineering and configuration
│   └── models/          # Model training and evaluation scripts
├── scripts/             # Utility scripts
├── tests/               # Unit and integration tests
└── docs/                # Documentation
```

## Setup

1. Clone the repository
2. Install dependencies (using pip or poetry)
3. Run the data preprocessing pipeline:
   ```
   python -m ml.preprocessing
   ```
4. Train the model:
   ```
   python -m ml.models.train
   ```
5. Evaluate the model:
   ```
   python -m ml.models.evaluation
   ```

## Usage

The project consists of three main components:

1. **Data Preprocessing** (`ml.preprocessing`): Loads log data, validates consistency, extracts features, and saves them using joblib
2. **Model Training** (`ml.models.train`): Loads preprocessed data, trains an Isolation Forest model, and saves the trained model
3. **Model Evaluation** (`ml.models.evaluation`): Loads the trained model and test data, evaluates performance, and reports metrics

## Testing

Run the available tests with:
```
pytest tests/
```

## License

MIT License - See LICENSE file for details.
