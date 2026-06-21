"""
AnalystLab Africa ML Internship — Week 7: Model Deployment
Diabetes Prediction API

A Flask REST API that serves a trained Random Forest model for predicting
diabetes risk based on diagnostic measurements.

Run locally with:
    python app.py

Then send requests to http://127.0.0.1:5000/predict
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import json
import os

app = Flask(__name__)

# ── Load model artifacts at startup ──────────────────────────────────────
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')

model = joblib.load(os.path.join(MODEL_DIR, 'diabetes_model.joblib'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.joblib'))
imputer = joblib.load(os.path.join(MODEL_DIR, 'imputer.joblib'))

with open(os.path.join(MODEL_DIR, 'metadata.json')) as f:
    metadata = json.load(f)

FEATURE_NAMES = metadata['feature_names']

print("✅ Model, scaler, and imputer loaded successfully.")
print(f"✅ Expected features: {FEATURE_NAMES}")


# ── Helper: validate and prepare input ───────────────────────────────────
def prepare_input(data: dict):
    """Validate incoming JSON and convert to a model-ready array."""
    missing = [f for f in FEATURE_NAMES if f not in data]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    row = pd.DataFrame([{f: data[f] for f in FEATURE_NAMES}])

    # Treat biologically impossible zeros as missing, same as training
    zero_as_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in zero_as_missing:
        if row.at[0, col] == 0:
            row.at[0, col] = np.nan

    row_imputed = pd.DataFrame(imputer.transform(row), columns=FEATURE_NAMES)
    row_scaled = scaler.transform(row_imputed)
    return row_scaled


# ── Routes ────────────────────────────────────────────────────────────────
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'project': 'Diabetes Prediction API',
        'status': 'running',
        'endpoints': {
            '/predict': 'POST — send patient data, get a prediction',
            '/health': 'GET — check API status',
            '/model-info': 'GET — model details and performance metrics'
        }
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model_loaded': True})


@app.route('/model-info', methods=['GET'])
def model_info():
    return jsonify({
        'model_type': 'Random Forest Classifier (tuned via GridSearchCV)',
        'features_required': FEATURE_NAMES,
        'target': 'Outcome (0 = No Diabetes, 1 = Diabetes)',
        'performance_metrics': metadata['model_metrics'],
        'feature_ranges_seen_in_training': metadata['feature_ranges']
    })


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON body received'}), 400

        X = prepare_input(data)

        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0][1])

        result = {
            'prediction': prediction,
            'prediction_label': 'Diabetes' if prediction == 1 else 'No Diabetes',
            'probability_of_diabetes': round(probability, 4),
            'confidence': round(probability if prediction == 1 else 1 - probability, 4),
            'input_received': data
        }
        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
