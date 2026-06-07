# AnalystLab Africa — Machine Learning Internship

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-green)

Documenting my weekly progress through the AnalystLab Africa
Machine Learning Internship Program.

---

## 📁 Weekly Progress

| Week | Topic | Folder | Status |
|---|---|---|---|
| Week 1-2 | Data Preprocessing & EDA | `week1-2-eda/` | ✅ Complete |
| Week 3 | Machine Learning Fundamentals | `week3-ml-fundamentals/` | ✅ Complete |
| Week 4 | Supervised Learning | `week4-supervised-learning/` | ✅ Complete |
| Week 5 | Advanced Machine Learning | `week5-advanced-ml/` | ✅ Complete |

---

## Week 1-2: Data Preprocessing & EDA
**Notebook:** [EDA_Notebook.ipynb](week1-2-eda/EDA_Notebook.ipynb)
**Datasets:** Titanic | IMDB 50K Reviews

**Key Findings:**
- Women on the Titanic survived at 74% vs 19% for men
- IMDB dataset is perfectly balanced — 25,000 positive, 25,000 negative
- Cabin dropped (77% missing); Age imputed with median

![Titanic EDA](week1-2-eda/images/titanic_eda.png)

---

## Week 3: Machine Learning Fundamentals
**Notebook:** [Week3_ML_Fundamentals.ipynb](week3-ml-fundamentals/Week3_ML_Fundamentals.ipynb)

**Key Results:**
| Model | Accuracy |
|---|---|
| Logistic Regression | 80.45% |
| Decision Tree (depth=4) | 78.77% |
| Random Forest | 81.56% |
| IMDB Sentiment (TF-IDF + LR) | 86.40% |

![Overfitting Chart](week3-ml-fundamentals/images/overfit_underfit.png)

---

## Week 4: Supervised Learning
**Notebook:** [Week4_Supervised_Learning.ipynb](week4-supervised-learning/Week4_Supervised_Learning.ipynb)
**Report:** [Week4_Evaluation_Report.docx](week4-supervised-learning/Week4_Evaluation_Report.docx)

**Task 1 — Linear Regression (Boston Housing)**
- RMSE: $5.14k | R²: 0.64
- Top features: rooms (↑ price), lower-status % (↓ price)

**Task 2 — Logistic Regression (Titanic)**
- Accuracy: 80.45%
- Gender was the strongest survival predictor

![Regression Results](week4-supervised-learning/images/regression_results.png)

---

## Week 5: Advanced Machine Learning
**Notebook:** [Week5_Advanced_ML.ipynb](week5-advanced-ml/Week5_Advanced_ML.ipynb)
**Report:** [Week5_Performance_Report.docx](week5-advanced-ml/Week5_Performance_Report.docx)

**Models trained and compared:**
| Model | Test Accuracy | CV Accuracy |
|---|---|---|
| Decision Tree | 82.12% | 77.26% |
| Random Forest | 80.45% | 78.39% |
| Gradient Boosting | 79.89% | 81.19% |
| RF Tuned (GridSearch) | 78.77% | 82.88% |
| GB Tuned (GridSearch) | 79.89% | 82.60% |

**Best model:** Tuned Random Forest — highest CV accuracy (82.88%), most reliable generalisation

**Key insight:** Cross-validation accuracy is a more trustworthy evaluation metric than single test accuracy. The Decision Tree had the highest test accuracy but the lowest CV score — a sign of overfitting.

![CV Comparison](week5-advanced-ml/images/week5_cv_comparison.png)

---

## 🛠 Tools & Libraries
Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Jupyter

## ▶ How to Run
1. Clone: `git clone https://github.com/YOUR_USERNAME/analystlab-ml-internship.git`
2. Install: `pip install -r requirements.txt`
3. Open any notebook in Jupyter and run all cells

## 📂 Data Sources
- [Titanic — Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) — included
- [IMDB 50K Reviews — Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) — not included (60MB), download and run notebook to regenerate
- [Boston Housing — GitHub](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv) — included
