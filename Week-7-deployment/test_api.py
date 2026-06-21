"""
Test script for the Diabetes Prediction API.
Run this after starting app.py in a separate terminal:

    Terminal 1: python app.py
    Terminal 2: python test_api.py
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def print_response(title, response):
    print(f"\n{'='*55}")
    print(f"  {title}")
    print(f"{'='*55}")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))


def test_home():
    r = requests.get(f"{BASE_URL}/")
    print_response("GET / (home)", r)


def test_health():
    r = requests.get(f"{BASE_URL}/health")
    print_response("GET /health", r)


def test_model_info():
    r = requests.get(f"{BASE_URL}/model-info")
    print_response("GET /model-info", r)


def test_predict_high_risk():
    payload = {
        "Pregnancies": 6,
        "Glucose": 148,
        "BloodPressure": 72,
        "SkinThickness": 35,
        "Insulin": 0,
        "BMI": 33.6,
        "DiabetesPedigreeFunction": 0.627,
        "Age": 50
    }
    r = requests.post(f"{BASE_URL}/predict", json=payload)
    print_response("POST /predict (high-risk profile)", r)


def test_predict_low_risk():
    payload = {
        "Pregnancies": 1,
        "Glucose": 85,
        "BloodPressure": 66,
        "SkinThickness": 29,
        "Insulin": 0,
        "BMI": 26.6,
        "DiabetesPedigreeFunction": 0.351,
        "Age": 31
    }
    r = requests.post(f"{BASE_URL}/predict", json=payload)
    print_response("POST /predict (low-risk profile)", r)


def test_predict_missing_fields():
    payload = {"Pregnancies": 1, "Glucose": 85}
    r = requests.post(f"{BASE_URL}/predict", json=payload)
    print_response("POST /predict (missing fields — should error)", r)


if __name__ == "__main__":
    print("Running Diabetes Prediction API test suite...")
    print(f"Target: {BASE_URL}")

    test_home()
    test_health()
    test_model_info()
    test_predict_high_risk()
    test_predict_low_risk()
    test_predict_missing_fields()

    print(f"\n{'='*55}")
    print("  All tests completed.")
    print(f"{'='*55}")
