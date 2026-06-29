# AnalystLab Africa — Machine Learning Internship

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

Documenting my weekly progress through the AnalystLab Africa Machine Learning
Internship Program (Batch A: May 1 — July 1, 2026).

---

## 📁 Weekly Progress

| Week | Topic | Folder | Status |
|---|---|---|---|
| Week 1-2 | Data Preprocessing & EDA | `week1-2-eda/` | Complete |
| Week 3 | Machine Learning Fundamentals | `week3-ml-fundamentals/` | 
| Week 4 | Supervised Learning | `week4-supervised-learning/` | 
| Week 5 | Advanced Machine Learning | `week5-advanced-ml/` | 
| Week 6 | Model Tuning & Validation | `week6-model-tuning/` | 
| Week 7 | Model Deployment | `Week-7-deployment/` | 
| Week 8 | Capstone Project | `week8-capstone/` |

---

## Week 1-2: Data Preprocessing & EDA
**Notebook:** [EDA_Notebook.ipynb](week1-2-eda/EDA_Notebook.ipynb)
**Datasets:** Titanic | IMDB 50K Reviews

Women on the Titanic survived at 74% vs 19% for men. IMDB dataset is perfectly
balanced — 25,000 positive, 25,000 negative.

![Titanic EDA](week1-2-eda/images/titanic_eda.png)

---

## Week 3: Machine Learning Fundamentals
**Notebook:** [Week3_ML_Fundamentals.ipynb](week3-ml-fundamentals/Week3_ML_Fundamentals.ipynb)

| Model | Accuracy |
|---|---|
| Logistic Regression | 80.45% |
| Random Forest | 81.56% |
| IMDB Sentiment (TF-IDF + LR) | 86.40% |

![Overfitting Chart](week3-ml-fundamentals/images/overfit_underfit.png)

---

## Week 4: Supervised Learning
**Notebook:** [Week4_Supervised_Learning.ipynb](week4-supervised-learning/Week4_Supervised_Learning.ipynb)

**Linear Regression (Boston Housing):** RMSE $5.14k, R² 0.64
**Logistic Regression (Titanic):** Accuracy 80.45%

![Regression Results](week4-supervised-learning/images/regression_results.png)

---

## Week 5: Advanced Machine Learning
**Notebook:** [Week5_Advanced_ML.ipynb](week5-advanced-ml/Week5_Advanced_ML.ipynb)

| Model | CV Accuracy |
|---|---|
| Decision Tree | 77.26% |
| Random Forest | 78.39% |
| Gradient Boosting | 81.19% |
| RF Tuned (GridSearch) | 82.88% |

![CV Comparison](week5-advanced-ml/images/week5_cv_comparison.png)

---

## Week 6: Model Tuning & Validation
**Notebook:** [Week6_Model_Tuning_Validation.ipynb](week6-model-tuning/Week6_Model_Tuning_Validation.ipynb)
**Dataset:** Pima Indians Diabetes Database

| Model | CV Accuracy |
|---|---|
| Baseline (Random Forest) | 76.38% ± 2.14% |
| Grid Search Tuned | 78.01% ± 2.58% |
| Random Search Tuned | 78.18% ± 2.38% |

Cross-validation accuracy improved after tuning even when single test-set
accuracy dropped — CV is the reliable selection metric.

![Bias-Variance Tradeoff](week6-model-tuning/images/week6_bias_variance.png)

---

## Week 7: Model Deployment
**Source code:** [Week-7-deployment/app.py](Week-7-deployment/app.py)
**Documentation:** [API_DOCUMENTATION.md](Week-7-deployment/API_DOCUMENTATION.md)

The Week 6 tuned Random Forest deployed as a Flask REST API. The model,
scaler, and imputer are saved with joblib and loaded at startup.

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | API info |
| `/health` | GET | Status check |
| `/model-info` | GET | Model metrics and feature details |
| `/predict` | POST | Send patient data, get diabetes risk prediction |

Run locally:
```bash
cd Week-7-deployment
pip install -r requirements.txt
python app.py
```

---

## Week 8: Capstone Project — Student Academic Performance Prediction
**Notebook:** [Week8_Capstone_Student_Performance.ipynb](week8-capstone/Week8_Capstone_Student_Performance.ipynb)
**Report:** [Week8_Capstone_Report.docx](week8-capstone/Week8_Capstone_Report.docx)
**Domain:** Education Analytics

### Problem
Predict whether a secondary school student will pass or fail their final exam,
and predict their exact final grade, using features a school can collect at
the start of the term.

### Results — Classification (Pass/Fail)
| Model | ROC-AUC | CV Accuracy |
|---|---|---|
| Logistic Regression | **95.74%** | **90.25%** |
| Decision Tree | 94.07% | 88.25% |
| Random Forest | 95.56% | 90.00% |
| Gradient Boosting | 94.61% | 89.13% |

**Best model: Logistic Regression** — 96% recall, meaning it correctly
identified 96% of students who would fail.

### Results — Regression (Grade Prediction)
| Metric | Score |
|---|---|
| RMSE | 1.737 |
| R² | 0.886 |

### Key Findings
- Prior grades (G1, G2) are the strongest predictors — early warning signals
  are available well before the final exam
- Each past failure reduces expected final grade by ~2.8 points on average
- Parental education level correlates with 3+ grade point difference in outcomes
- Internet access and urban location both improve performance measurably

![Capstone EDA](week8-capstone/images/capstone_eda.png)
![Model Comparison](week8-capstone/images/capstone_model_comparison.png)

---

## 🛠 Tools & Libraries
Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Jupyter ·
Flask · Joblib

## ▶ How to Run
1. Clone: `git clone https://github.com/vincent777756/Analystlab-ml-internship.git`
3. Install: `pip install -r requirements.txt`
4. Open any notebook in Jupyter and run all cells

## 📂 Data Sources
- [Titanic — Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) — included
- [IMDB 50K Reviews — Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) — not included (60MB), download and run notebook to regenerate
- [Boston Housing — GitHub](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv) — included
- [Pima Indians Diabetes — Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) — included
- [Student Performance — UCI](https://archive.ics.uci.edu/dataset/320/student+performance) — included
