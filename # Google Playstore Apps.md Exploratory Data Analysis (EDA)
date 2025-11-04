# Google Playstore Apps — Exploratory Data Analysis

**Repository:** `2024/14_Keggalgoogle_EDA.ipynb`
**Author:** **shafiq73**
**Notebook:** `14_Keggalgoogle_EDA.ipynb`

---

## Project Summary

This project performs a thorough Exploratory Data Analysis (EDA) on the **Google Playstore Apps** dataset (sourced from Kaggle). The analysis investigates app categories, ratings, installs, pricing, reviews, and other app metadata to extract insights, find data quality issues, and prepare the dataset for further modeling or reporting.

## Goals

* Clean and preprocess the Playstore dataset.
* Explore distributions of ratings, installs, and prices across categories.
* Visualize relationships (e.g., rating vs. installs, category-wise averages).
* Identify missing values and inconsistent formatting.
* Provide recommendations and next steps for modeling or product decisions.

## Dataset

**Source:** Kaggle — Google Playstore Apps dataset.
**Filename (expected):** `googleplaystore.csv` (or similarly named CSV used in the notebook).

> If the raw dataset file is not present in the repo, download it from Kaggle and place it in the notebook’s working directory.

## Notebook Overview

The notebook `14_Keggalgoogle_EDA.ipynb` is structured into the following sections:

1. **Imports & Setup** — Load pandas, numpy, matplotlib, seaborn and set plotting defaults.
2. **Load Data** — Read CSV(s) and display initial shape and sample rows.
3. **Data Cleaning** — Fix column names, handle missing values, convert types (e.g., `Installs`, `Price`, `Rating`), remove duplicates, and handle outliers.
4. **Univariate Analysis** — Histograms and summary stats for numeric features like `Rating`, `Reviews`, `Installs`, `Price`.
5. **Categorical Analysis** — Counts and comparisons across `Category`, `Content Rating`, and `Genres`.
6. **Bivariate Analysis** — Scatterplots and boxplots investigating relationships such as `Rating` vs `Installs`, `Price` by `Category`.
7. **Text / Reviews Insights** — Basic checks on review counts and free vs paid apps.
8. **Key Findings & Recommendations** — Short summary and suggestions for next steps.

## Key Findings (example highlights)

* Many apps contain inconsistent formatting in `Installs` (commas, + signs) and `Price` (currency symbols) which were cleaned.
* A non-trivial number of missing `Rating` or `Category` values were found and handled.
* Certain categories show consistently higher ratings and installs — good candidates for deeper market analysis.

> Note: Exact findings depend on the dataset version. See the notebook’s final cells for the concrete numbers and charts.

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/shafiq73/2024.git
cd 2024
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# or, if requirements.txt not present:
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

4. Open the notebook in Jupyter or JupyterLab:

```bash
jupyter notebook 14_Keggalgoogle_EDA.ipynb
```

## Dependencies (suggested)

* Python 3.8+
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn (optional — for any modeling steps)

You can generate a `requirements.txt` with the exact versions used if you want reproducibility.

## Suggested Improvements / Next Steps

* Add a `data/` folder and include a small sample CSV or a script to download the data automatically (if licensing allows).
* Create a `requirements.txt` with pinned versions.
* Convert the notebook into a reproducible pipeline (e.g., using `papermill`, `nbconvert`, or an ML pipeline tool).
* Add a `results/` folder containing exported charts (PNG) and a short PDF report summarizing key metrics for stakeholders.
* Expand analysis into predictive modeling (e.g., predict app rating or installs) using feature engineering.

## License

If you want to attach a license, include a `LICENSE` file. Common choices: MIT, Apache-2.0.

## Contact

**Author / GitHub:** `shafiq73`
**Email:** (add your contact email here if you want people to reach out)

---

*If you want this README in Urdu, or want me to add badges, example charts, or a `requirements.txt`, tell me and I'll update it.*
