# Student Academic Performance Prediction
### AnalystLab Africa ML Internship — Week 8: Capstone Project

## Problem Statement
Predict whether a secondary school student will **pass or fail** their final exam, and predict their **exact final grade**, using demographic, social, and academic features collected at the start of the school year.

Early identification of at-risk students enables targeted intervention before exam season — a direct, measurable impact on educational outcomes.

---

## Dataset
Based on the UCI Student Performance Dataset structure (Cortez & Silva, 2008).

| Attribute | Detail |
|---|---|
| Records | 1,000 students |
| Features | 18 (demographic, social, academic) |
| Classification target | `passed` — 1 if final grade ≥ 10, 0 otherwise |
| Regression target | `G3` — final grade (0–20) |
| Class balance | 70.5% passed, 29.5% failed |

---

## Results

### Classification (Pass/Fail Prediction)
| Model | ROC-AUC | CV Accuracy |
|---|---|---|
| Logistic Regression | **95.74%** | **90.25%** |
| Decision Tree | 94.07% | 88.25% |
| Random Forest | 95.56% | 90.00% |
| Gradient Boosting | 94.61% | 89.13% |

**Best model: Logistic Regression** — highest ROC-AUC and CV accuracy, with 96% recall (catches 96% of students who will fail).

### Regression (Grade Prediction)
| Metric | Score |
|---|---|
| RMSE | 1.737 |
| MAE | 1.361 |
| R² | 0.886 |

---

## Key Findings
- Prior grades (G1, G2) are the strongest predictors of final performance
- Past failures and absences are directly actionable early warning signals
- Higher parental education correlates with 3+ grade points better outcomes
- Students with internet access and urban addresses consistently outperform peers
- Weekday alcohol consumption has a measurable negative effect on grades

## Recommendations
- Flag students with G1 < 8 or absences > 15 for immediate counselling
- Target study support programmes at students studying less than 2 hours weekly
- Prioritise internet access in rural schools
- Deploy as a web tool for teachers to get instant at-risk predictions

---

## Project Structure
```
week8-capstone/
├── Week8_Capstone_Student_Performance.ipynb
├── Week8_Capstone_Report.docx
├── student_performance.csv
├── README.md
└── images/
    ├── capstone_eda.png
    ├── capstone_correlation.png
    ├── capstone_model_comparison.png
    ├── capstone_best_model.png
    ├── capstone_feature_importance.png
    └── capstone_regression.png
```

## How to Run
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook Week8_Capstone_Student_Performance.ipynb
```

## Tools & Libraries
Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Jupyter
