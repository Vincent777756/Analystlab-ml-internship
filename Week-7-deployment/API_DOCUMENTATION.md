# Diabetes Prediction API — Documentation

## Project Title
**Diabetes Prediction API** — AnalystLab Africa ML Internship, Week 7: Model Deployment

## Model Description
A Random Forest Classifier trained on the Pima Indians Diabetes Database, tuned via GridSearchCV in Week 6 (`max_depth=6, max_features='log2', min_samples_split=5, n_estimators=100`). The model predicts whether a patient is likely to have diabetes based on 8 diagnostic measurements.

| Metric | Score |
|---|---|
| Accuracy | 72.08% |
| Precision | 63.41% |
| Recall | 48.15% |
| F1 Score | 54.74% |
| ROC-AUC | 80.87% |

The model, the `StandardScaler`, and the `SimpleImputer` used during training were all saved with `joblib` and are loaded together at API startup so that incoming requests are preprocessed identically to the training data (zeros in `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, and `BMI` are treated as missing and median-imputed, then scaled).

## Input Features

| Field | Type | Description |
|---|---|---|
| `Pregnancies` | integer | Number of times pregnant |
| `Glucose` | float | Plasma glucose concentration |
| `BloodPressure` | float | Diastolic blood pressure (mm Hg) |
| `SkinThickness` | float | Triceps skin fold thickness (mm) |
| `Insulin` | float | 2-Hour serum insulin (mu U/ml) |
| `BMI` | float | Body mass index |
| `DiabetesPedigreeFunction` | float | Diabetes pedigree function (genetic risk score) |
| `Age` | integer | Age in years |

**Note:** A value of `0` for `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, or `BMI` is treated as a missing reading (consistent with how the training data was cleaned) and will be imputed with the training-set median for that feature.

## Endpoints

### `GET /`
Returns basic API info and a list of available endpoints.

### `GET /health`
Returns API status. Use this to confirm the API and model are running before sending prediction requests.

### `GET /model-info`
Returns model type, required features, target description, performance metrics, and the feature value ranges seen during training (useful for sanity-checking input values).

### `POST /predict`
Accepts a JSON body with all 8 required features and returns a prediction.

---

## Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  }'
```

Or in Python:

```python
import requests

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
response = requests.post("http://127.0.0.1:5000/predict", json=payload)
print(response.json())
```

## Example Response

```json
{
  "prediction": 1,
  "prediction_label": "Diabetes",
  "probability_of_diabetes": 0.6791,
  "confidence": 0.6791,
  "input_received": {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  }
}
```

## Error Response Example

If a required field is missing:

```json
{
  "error": "Missing required fields: ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']"
}
```
Returned with HTTP status `400 Bad Request`.

---

## How to Run the API

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the API
```bash
python app.py
```
You should see:
```
✅ Model, scaler, and imputer loaded successfully.
 * Running on http://127.0.0.1:5000
```

### 3. Test it
In a second terminal:
```bash
python test_api.py
```
This runs all 6 endpoint tests automatically (home, health, model-info, two predictions, and an error case) and prints the results.

Alternatively, test manually with `curl` (see Example Request above) or a tool like Postman.

---

## Assumptions & Limitations

- **Development server only.** This uses Flask's built-in development server (`debug=False` for stability), which is not suitable for production traffic. For real deployment, use a WSGI server such as Gunicorn behind Nginx, or a managed platform (Render, Railway, AWS Elastic Beanstalk, etc.).
- **No authentication.** The API currently accepts any request with no API key or rate limiting — not suitable for a public production endpoint as-is.
- **Model accuracy ceiling.** At 72% accuracy and 48% recall, the model misses roughly half of actual diabetes cases. This is a known limitation of the Pima Indians dataset with only 8 features and 768 samples — it should be treated as a decision-support demo, not a diagnostic tool.
- **Input validation is basic.** The API checks that all required fields are present but does not currently validate that values fall within medically plausible ranges (e.g. Age between 0 and 120).
- **Zero handling.** Because zeros are treated as missing for 5 specific features, a genuinely measured value of 0 (which is implausible for those fields anyway) cannot be passed through — it will always be imputed.
