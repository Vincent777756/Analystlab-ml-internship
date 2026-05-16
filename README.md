# AnalystLab Africa ML Internship — Week 1-2
## Data Preprocessing & Exploratory Data Analysis

### Datasets
- [Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset) — 891 rows, 12 features
- [IMDB Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) — 50,000 reviews

### Tools Used
Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn

### Key Findings
- Women on the Titanic survived at 74% vs. 19% for men
- 1st class passengers had 63% survival vs. 24% in 3rd class
- IMDB dataset is perfectly balanced (50/50 positive/negative)

### EDA Visuals
![Titanic EDA](images/titanic_eda.png)
![IMDB EDA](images/imdb_eda.png)

### How to Run
1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Open `EDA_Notebook.ipynb` in Jupyter

## Data

| Dataset | Source | Status |
|---|---|---|
| Titanic | [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) | `data/titanic_cleaned.csv` included |
| IMDB 50K Reviews | [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) | Not included (60MB) — regenerate below |

### Regenerating the IMDB cleaned dataset
1. Download `IMDB_Dataset.csv` from the Kaggle link above
2. Place it in the `data/` folder
3. Run all cells in `EDA_Notebook.ipynb` — it will produce `imdb_cleaned.csv` automatically
