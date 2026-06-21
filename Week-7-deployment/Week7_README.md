# Week 7: Model Deployment — Diabetes Prediction API

AnalystLab Africa ML Internship — Week 7 deliverable.

A trained Random Forest model (from Week 6's tuning work) deployed as a REST API using Flask, so that any application can send patient data and receive a diabetes risk prediction in real time.

## Project Structure

```
week7-deployment/
├── app.py                    # Flask API source code
├── test_api.py                # Python test script (tests all endpoints)
├── test_results.txt           # Verified output from a live test run
├── requirements.txt            # Python dependencies
├── API_DOCUMENTATION.md        # Full API documentation
├── model/
│   ├── diabetes_model.joblib   # Trained Random Forest model
│   ├── scaler.joblib            # StandardScaler fitted on training data
│   ├── imputer.joblib           # SimpleImputer fitted on training data
│   └── metadata.json             # Feature names, ranges, and model metrics
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the API
python app.py

# 3. In a separate terminal, run the test suite
python test_api.py
```

The API will be live at `http://127.0.0.1:5000`.

## What This Demonstrates

- **Model persistence:** the tuned Random Forest from Week 6, along with its scaler and imputer, saved with `joblib` so it can be loaded and used without retraining
- **API design:** four endpoints (`/`, `/health`, `/model-info`, `/predict`) with proper request validation and JSON error handling
- **Testing:** both manual `curl` testing and an automated Python test script covering normal predictions and error cases
- **Documentation:** a full API reference so anyone (including a non-technical reviewer) can understand and use the API

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for full endpoint details, example requests/responses, and known limitations.

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | 72.08% |
| Precision | 63.41% |
| Recall | 48.15% |
| F1 Score | 54.74% |
| ROC-AUC | 80.87% |

Model: Random Forest Classifier, tuned via GridSearchCV (`max_depth=6, max_features='log2', min_samples_split=5, n_estimators=100`) — see [Week 6](../week6-model-tuning/) for the full tuning process.
